# run with interactive runner and testing tool via
# > python interactive_runner.py python testing_tool.py 0 -- python prob2.py
import math
import sys

CENTER = 'CENTER'
HIT = 'HIT'
MISS = 'MISS'
WRONG = 'WRONG'

def throw_dart(i, j):
    print('{} {}'.format(i, j))
    sys.stdout.flush()
    return input()


def main():
    T, A, B = [int(_) for _ in input().split(' ')]

    N = 10 ** 9
    for test_idx in range(1, T + 1):
        # find a corner
        grid_size = math.ceil(2 * N / A)

        response = None
        for i in range(grid_size + 1):
            x = min(-N + i * A, N)
            for j in range(grid_size + 1):
                y = min(-N + j * A, N)

                if abs(x) == abs(y) == N:
                    continue

                response = throw_dart(x, y)
                if response in [CENTER, HIT]:
                    break
            if response in [CENTER, HIT]:
                break

        if response is None:
            raise ValueError('had a response of None')
        elif response == CENTER:
            # one of the corners was the center, not bad
            continue
        else:
            know_center = False
            # we know a point; binary search to find the elements along the x
            # and y directions that are the edges of the circle

            # + y
            if throw_dart(x, N) == HIT:
                y_plus = N
            else:
                lft, rgt = y, N
                while rgt - lft > 1:
                    mp = (lft + rgt) // 2
                    resp_mp = throw_dart(x, mp)
                    if resp_mp == CENTER:
                        know_center = True
                        break
                    elif resp_mp == HIT:
                        lft = mp
                    else:
                        rgt = mp

                if know_center:
                    continue

                y_plus = lft

            # - y
            if throw_dart(x, -N) == HIT:
                y_minus = -N
            else:
                lft, rgt = -N, y
                while rgt - lft > 1:
                    mp = (lft + rgt) // 2
                    resp_mp = throw_dart(x, mp)
                    if resp_mp == CENTER:
                        know_center = True
                        break
                    elif resp_mp == HIT:
                        rgt = mp
                    else:
                        lft = mp

                if know_center:
                    continue

                y_minus = rgt

            # + x
            if throw_dart(N, y) == HIT:
                x_plus = N
            else:
                lft, rgt = x, N
                while rgt - lft > 1:
                    mp = (lft + rgt) // 2
                    resp_mp = throw_dart(mp, y)
                    if resp_mp == CENTER:
                        know_center = True
                        break
                    elif resp_mp == HIT:
                        lft = mp
                    else:
                        rgt = mp

                if know_center:
                    continue

                x_plus = lft

            # - x
            if throw_dart(-N, y) == HIT:
                x_minus = -N
            else:
                lft, rgt = -N, x
                while rgt - lft > 1:
                    mp = (lft + rgt) // 2
                    resp_mp = throw_dart(mp, y)
                    if resp_mp == CENTER:
                        know_center = True
                        break
                    elif resp_mp == HIT:
                        rgt = mp
                    else:
                        lft = mp

                if know_center:
                    continue

                x_minus = rgt

        x_mid = (x_plus + x_minus) // 2
        y_mid = (y_plus + y_minus) // 2

        resp_mid = throw_dart(x_mid, y_mid)
        if resp_mid != CENTER:
            raise ValueError("fuck")


if __name__ == '__main__':
    main()
