def build_cond(p_x, p_y, d):
    p_x = int(p_x)
    p_y = int(p_y)

    def cond(x, y):
        if d == 'N':
            return y > p_y
        elif d == 'S':
            return y < p_y
        elif d == 'E':
            return x > p_x
        else:
            return x < p_x

    return cond


def main():
    T = int(input())

    for i_test_case in range(T):
        P, Q = [int(_) for _ in input().split(' ')]

        x_vals = [0] * (Q + 1)
        y_vals = [0] * (Q + 1)
        for i_person in range(P):
            x, y, d = input().split(' ')
            x = int(x)
            y = int(y)

            if d == 'N':
                for i in range(y + 1, Q + 1):
                    y_vals[i] += 1
            elif d == 'S':
                for i in range(0, y):
                    y_vals[i] += 1
            elif d == 'E':
                for i in range(x + 1, Q + 1):
                    x_vals[i] += 1
            else:
                for i in range(0, y):
                    x_vals[i] += 1

        x_c = x_vals.index(max(x_vals))
        y_c = y_vals.index(max(y_vals))

        print(
            "Case #{}: {} {}".format(i_test_case + 1, x_c, y_c))


if __name__ == '__main__':
    main()
