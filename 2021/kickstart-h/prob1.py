from string import ascii_lowercase

letter_map = {c: i for (i, c) in enumerate(ascii_lowercase)}

def main():
    T = int(input())

    for x in range(1, T + 1):
        S = input()
        F = input()

        s = [letter_map[s] for s in S]
        f = [letter_map[f] for f in F]

        y = sum(
            min(
                min(
                    (s_now - f_now) % 26,
                    (f_now - s_now) % 26
                )
                for f_now in f
            )
            for s_now in s
        )

        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()
