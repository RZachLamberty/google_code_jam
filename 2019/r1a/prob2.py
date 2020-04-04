import sys


def main():
    T, N, M = [int(_) for _ in input().split(' ')]

    for i_test_case in range(T):
        options = None
        lower_bound = 0
        answer = '-1'
        for n in [17, 16, 13, 11, 7, 5, 3]:
            print(' '.join([str(n) for i in range(18)]))
            sys.stdout.flush()

            x = sum([int(_) for _ in input().split(' ')])
            lower_bound = max(lower_bound, x)
            mod = x % n

            options_now = {i for i in range(lower_bound, M + 1) if i % n == mod}
            if options is None:
                options = options_now
            else:
                options.intersection_update(options_now)

            # debug
            # print("for me: len(options) = {}".format(len(options)))
            # if len(options) < 10:
            #     print('options = {}'.format(options))

            if len(options) == 1:
                # guess
                print(options.pop())
                sys.stdout.flush()
                answer = input()
                break

        if answer == '1':
            continue
        elif answer == '-1':
            exit(1)


if __name__ == '__main__':
    main()
