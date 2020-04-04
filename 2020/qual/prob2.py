DEBUG = False


def debug(s):
    if DEBUG:
        print(s)


def main():
    T = int(input())

    for x in range(1, T + 1):
        S = [int(_) for _ in input()]

        debug(f'\n\nstarting case #{x}')
        debug(f'S = {S}')

        y = ''
        last_val = 0

        for next_val in S:
            delta = last_val - next_val

            debug(f'\ny = {y}')
            debug(f'last_val = {last_val}')
            debug(f'next_val = {next_val}')
            debug(f'delta = {delta}')

            if delta == 0:
                pass
            elif delta > 0:
                y += ')' * delta
            elif delta < 0:
                y += '(' * abs(delta)

            y += str(next_val)
            last_val = next_val

            debug(f'y becomes: {y}')

        y += ')' * last_val

        # x: the test case number (starting from 1)
        # y: the string S' defined above.
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()