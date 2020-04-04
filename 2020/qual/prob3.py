DEBUG = True


def debug(s):
    if DEBUG:
        print(s)


def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())

        debug(f'\n\n\nbeginning case {x}')
        debug(f'num activities N: {N}')

        times = sorted([[int(t) for t in input().split(' ')]
                        for _ in range(N)])

        debug(f'times = {times}')

        y = ''
        c_busy_until = None
        j_busy_until = None
        for (s, e) in times:
            if (c_busy_until is None or c_busy_until <= s):
                c_busy_until = e
                y += 'C'
            elif (j_busy_until is None or j_busy_until <= s):
                j_busy_until = e
                y += 'J'
            else:
                y = 'IMPOSSIBLE'
                break

        # x: the test case number (starting from 1)
        # y: IMPOSSIBLE if there is no valid schedule according to the above
        #    rules, or a string of exactly N characters otherwise. The i-th
        #    character in y must be C if the i-th activity is assigned to
        #    Cameron in your proposed schedule, and J if it is assigned to
        #    Jamie.
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()