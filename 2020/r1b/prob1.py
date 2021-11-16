LAST_JUMPS = {(0, 1): 'N',
              (1, 0): 'E',
              (0, -1): 'S',
              (-1, 0): 'W'}

def make_jump(X, Y):
    global LAST_JUMPS

    try:
        return LAST_JUMPS[X, Y], (0, 0)
    except KeyError:
        pass

    if is_odd(X):
        Y_new = Y / 2
        for sign in [-1, 1]:
            X_new = (X - sign) / 2

            if is_odd(X_new + Y_new):
                return ('E' if sign == 1 else 'W'), (X_new, Y_new)
    else:
        X_new = X / 2
        for sign in [-1, 1]:
            Y_new = (Y - sign) / 2

            if is_odd(X_new + Y_new):
                return ('N' if sign == 1 else 'S'), (X_new, Y_new)


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return not is_even(x)


def main():
    T = int(input())
    for x in range(1, T + 1):
        X, Y = [int(_) for _ in input().split(' ')]

        if is_even(X + Y):
            y = 'IMPOSSIBLE'
        else:
            y = ''
            while True:
                jump_dir_str, (X, Y) = make_jump(X, Y)
                y += jump_dir_str
                if X == Y == 0:
                    break

        if y is None:
            raise ValueError('woopsies')

        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()
