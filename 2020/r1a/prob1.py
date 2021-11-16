import fnmatch
import re


def make_match(P):
    y = ''

    for p in P:
        if y == '' and p != '*':
            y = p
            continue

        # three options. the thing we've built so far (k) is a substring of p,
        # p is a substring of k, or we exit
        impossible = True
        for s0, s1 in [[y, p], [p, y]]:
            regex = fnmatch.translate(s0)
            pattern = re.sub('[\*]+$', '', s1)
            m = re.match(regex, pattern)
            if m:
                y = pattern[m.start(): m.end()]
                impossible = False
                break

        if impossible:
            return '*'

    return y.replace('*', '')


def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())
        P = [input() for i in range(N)]
        y = make_match(P)

        # k: any name containing at most 104 letters such that each Pi matches k
        #    according to the definition above
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()
