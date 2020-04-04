class Trie:
    def __init__(self, value, is_word_end=False):
        self.value = value
        self.is_word_end = is_word_end
        self.children = {}

    def add_word(self, word):
        c0, rest = word[0], word[1:]
        is_word_end = rest == ''

        try:
            child_trie = self.children[c0]
        except KeyError:
            self.children[c0] = Trie(c0, is_word_end)
            child_trie = self.children[c0]

        child_trie.is_word_end = child_trie.is_word_end or is_word_end
        if not is_word_end:
            child_trie.add_word(rest)

    def to_dict(self):
        return {k: v.to_dict() for (k, v) in self.children.items()}

    @property
    def is_root(self):
        return self.value is None

    def f(self):
        if self.children:
            r = sum([child_trie.f() for (child_key, child_trie) in
                     self.children.items()])
            if self.is_word_end:
                r += 1
            if not self.is_root and r >= 2:
                r -= 2
            return r
        else:
            return 1


def main():
    T = int(input())
    # T = 1

    for i_test_case in range(T):
        N = int(input())
        words = sorted([input()[::-1] for j_word in range(N)])
        # N = 6
        # words = ['CODEJAM', 'JAM', 'HAM', 'NALAM', 'HUM', 'NOLOM']
        # words = [w[::-1] for w in words]

        t = Trie(None)
        for word in words:
            t.add_word(word)

        print("Case #{}: {}".format(i_test_case, N - t.f()))


if __name__ == '__main__':
    main()
