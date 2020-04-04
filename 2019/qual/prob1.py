t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    orig = input().strip()
    a = orig.replace('4', '3')
    b = orig
    for j in '0123456789':
        b = b.replace(j, '1' if j == '4' else '0')
    b = str(int(b))
    print("Case #{}: {} {}".format(i, a, b))
