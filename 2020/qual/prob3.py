def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())

        # answer must be in provided order, but solution is easier in sorted
        # order. sort order function from here:
        # https://stackoverflow.com/questions/3382352
        times = [[int(t) for t in input().split(' ')]
                 for _ in range(N)]
        sort_order = sorted(range(len(times)), key=times.__getitem__)

        y = [''] * len(times)
        c_busy_until = 0
        j_busy_until = 0
        for i in sort_order:
            s, e = times[i]
            if c_busy_until <= s:
                c_busy_until = e
                y[i] = 'C'
            elif j_busy_until <= s:
                j_busy_until = e
                y[i] = 'J'
            else:
                y = 'IMPOSSIBLE'
                break

        if isinstance(y, list):
            y = ''.join(y)

        # x: the test case number (starting from 1)
        # y: IMPOSSIBLE if there is no valid schedule according to the above
        #    rules, or a string of exactly N characters otherwise. The i-th
        #    character in y must be C if the i-th activity is assigned to
        #    Cameron in your proposed schedule, and J if it is assigned to
        #    Jamie.
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()
