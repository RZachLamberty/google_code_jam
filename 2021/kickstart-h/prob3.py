class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node({self.data})'


class DoublyLinkedList:
    def __init__(self, debug=False):
        self.head = None
        self.tail = None
        self._interesting_nodes = None
        self.debug = debug

    def __repr__(self):
        if self.head is None:
            return 'DoublyLinkedList([])'
        else:
            node = self.head
            data = [node.data]
            while node.next is not None:
                node = node.next
                data.append(node.data)
            return f'DoublyLinkedList({data})'

    @property
    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data=data)
        new_node.prev = self.tail
        if self.is_empty:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def load_list(self, l):
        if not self.is_empty:
            raise ValueError('can only initialize from list if current list is empty')

        for x in l:
            self.append(data=x)

    def to_list(self):
        l = []
        node_now = self.head
        while node_now is not None:
            l.append(node_now.data)
            node_now = node_now.next
        return l

    def to_str(self):
        return ''.join([str(_) for _ in self.to_list()])

    def node_is_interesting(self, node):
        if node.next is None:
            return False
        else:
            this_val = node.data
            next_val = node.next.data
            return (this_val + 1) % 10 == next_val

    def mark_if_interesting(self, node):
        if self.node_is_interesting(node):
            self._interesting_nodes[node.data].add(node)
        else:
            for (i, i_list) in self.interesting_nodes.items():
                i_list.difference_update({node})

    @property
    def any_interesting(self):
        return any([len(node_list) > 0 for node_list in self.interesting_nodes.values()])

    @property
    def interesting_nodes(self):
        if self.is_empty:
            return {}
        if self._interesting_nodes is None:
            self._interesting_nodes = {j: set() for j in range(10)}
            node_now = self.head
            while node_now is not None:
                self.mark_if_interesting(node_now)
                node_now = node_now.next
        return self._interesting_nodes

    def replace(self, node_a):
        # assume node and next_node are both non-null
        node_b = node_a.next

        if node_b is None:
            raise ValueError("can't replace a tail node")

        new_node = Node(data=(node_a.data + 2) % 10)

        new_node.prev = node_a.prev
        try:
            node_a.prev.next = new_node
        except AttributeError:
            self.head = new_node

        new_node.next = node_b.next
        try:
            node_b.next.prev = new_node
        except AttributeError:
            self.tail = new_node

        # update the interesting nodes list
        remove_nodes = {node_a, node_b}
        for (i, i_list) in self.interesting_nodes.items():
            i_list.difference_update(remove_nodes)

        self.mark_if_interesting(new_node)
        if new_node.prev is not None:
            self.mark_if_interesting(new_node.prev)

    def collapse(self):
        while self.any_interesting:
            for i in range(10):
                i_list = self.interesting_nodes[i]
                while len(i_list) > 0:
                    if self.debug:
                        s_before = self.to_str()
                    repl_node = i_list.pop()
                    self.replace(repl_node)
                    if self.debug:
                        s_after = self.to_str()
                        print(f"{s_before} --> {s_after}")


def fix_string(S):
    s_to_list = [int(_) for _ in S]
    dll = DoublyLinkedList()
    dll.load_list(s_to_list)
    dll.collapse()
    return dll.to_str()


repls = {f'{i}{(i + 1) % 10}': str((i + 2) % 10)
         for i in range(10)}

def f_works(S):
    while True:
        l_before = len(S)

        if l_before == 1:
            break
        elif l_before in repls:
            break

        for (s_remove, s_replace) in repls.items():
            S = S.replace(s_remove, s_replace)

        l_after = len(S)

        if l_before == l_after:
            break
    return S


def main_test():
    import random
    for num_tests in range(10_000):
        s_test = ''.join(str(random.randint(0, 9)) for i in range(10))
        if f_works(s_test) != fix_string(s_test):
            print(s_test)
            raise ValueError()


def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())
        S = input()
        S = fix_string(S)
        print(f"Case #{x}: {S}")


if __name__ == '__main__':
    main_test()
