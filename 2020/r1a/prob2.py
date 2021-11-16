import functools
import random
from math import factorial


@functools.lru_cache()
def binomial(r, k):
    try:
        binom = factorial(r - 1) // factorial(k - 1) // factorial(r - k)
    except ValueError:
        binom = 0
    return binom


@functools.lru_cache()
def get_neighbors(r, k):
    neighbors = [(r - 1, k - 1), (r - 1, k),
                 (r, k - 1), (r, k + 1),
                 (r + 1, k), (r + 1, k + 1)]
    return [(r, k) for (r, k) in neighbors if 1 <= k <= r]


def do_random_walk(N, steps=500):
    r, k = 1, 1
    walk = [(r, k)]
    walk_sum = binomial(r, k)

    while walk_sum < N and len(walk) < steps:
        neighbors = list(set(get_neighbors(r, k)).difference(walk))
        try:
            r1, k1 = random.choice(neighbors)
        except IndexError:
            # no neighbors, couldn't self avoid
            break
        walk.append((r1, k1))
        walk_sum += binomial(r1, k1)
        r, k = r1, k1

    return walk, walk_sum


def pascal_walk(N):
    while True:
        walk, walk_sum = do_random_walk(N)
        if walk_sum == N:
            return walk


def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())

        walk = pascal_walk(N)

        # print Case #r:
        # Then, output your proposed Pascal walk of length S ≤ 500 using S
        # additional lines. The i-th of these lines must be ri ki where (ri,
        # ki) is the i-th position in the walk
        print("Case #{x}:".format(x=x))

        for (r, k) in walk:
            print("{r} {k}".format(r=r, k=k))


if __name__ == '__main__':
    main()
