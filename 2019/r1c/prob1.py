from collections import defaultdict


def main():
    T = int(input())

    for i_test_case in range(T):
        A = int(input())

        impossible = False
        casts = defaultdict(set)
        for i_adversary in range(A):
            if impossible:
                break

            # parse this adversary's program
            program = input()
            for (i, rsp) in enumerate(program):
                if impossible:
                    break
                casts[i].append(rsp)
                if len(casts[i]) == 3:
                    impossible = True

        if impossible:
            print("Case #{}: {}".format(i_test_case + 1, 'IMPOSSIBLE'))
        else:
            #


if __name__ == '__main__':
    main()
