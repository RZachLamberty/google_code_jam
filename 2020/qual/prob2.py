def main():
    T = int(input())

    for x in range(1, T + 1):
        S = [int(_) for _ in input()]

        y = ''
        last_val = 0

        for next_val in S:
            delta = last_val - next_val

            if delta == 0:
                pass
            elif delta > 0:
                y += ')' * delta
            elif delta < 0:
                y += '(' * abs(delta)

            y += str(next_val)
            last_val = next_val

        y += ')' * last_val

        # x: the test case number (starting from 1)
        # y: the string S' defined above.
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()