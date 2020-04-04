def main():
    T = int(input())

    for i_test_case in range(T):
        N, K = [int(_) for _ in input().split(" ")]

        c_skill = [int(_) for _ in input().split(' ')]
        d_skill = [int(_) for _ in input().split(' ')]

        fair_fights = 0
        for l in range(N):
            for r in range(l, N):
                c_sword = max(c_skill[l: r + 1])
                d_sword = max(d_skill[l: r + 1])
                if abs(d_sword - c_sword) <= K:
                    fair_fights += 1

        print(
            "Case #{}: {}".format(i_test_case + 1, fair_fights))


if __name__ == '__main__':
    main()
