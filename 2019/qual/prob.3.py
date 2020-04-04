import functools, math, string

num_test_cases = int(input())


def sieve(n):
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if prime[i]]


@functools.lru_cache()
def prime_factor(x):
    # get two prime factors
    primes = sieve(math.ceil(x ** .5))
    for p in primes:
        if x % p == 0:
            return p, x // p
    raise ValueError("shouldn't have reached this pt")
        

for case_num in range(1, num_test_cases + 1):
    N, L = [int(_) for _ in input().split(' ')]
    cipher = [int(_) for _ in input().split(' ')]

    message_ints = []
    lft, rt = None, None
    int_queue = [prime_factor(cipher[0])]
    c_prev = cipher[0]

    for c in cipher[1:]:
        if int_queue:
            if c == c_prev:
                int_queue.append(prime_factor(c))
            else:
                # we don't have an official left or right, unwind
                a, b = int_queue[-1]
                ult_rt, other = (a, b) if c % a == 0 else (b, a)
    
                # the k elems in int_queue represent k + 1 ints, the last of which is ult_rt
                to_add = list(reversed([ult_rt if i % 2 == 0 else other
                                        for i in range(len(int_queue) + 1)]))
                message_ints += to_add
                message_ints.append(c // ult_rt)
                int_queue = []
        else:
            lft = message_ints[-1]
            rt = c // lft
            message_ints.append(rt)

        c_prev = c

    primes = sorted(set(message_ints))
    lookup = dict(zip(primes, string.ascii_uppercase))

    msg = ''.join([lookup[p] for p in message_ints])
    print("Case #{}: {}".format(case_num, msg))
