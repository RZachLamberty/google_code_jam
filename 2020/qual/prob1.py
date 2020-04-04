def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())

        col_seen = {i: set() for i in range(1, N + 1)}
        row_seen = {i: set() for i in range(1, N + 1)}
        k = 0

        for row_idx in range(1, N + 1):
            row = [int(_) for _ in input().split(' ')]

            for (col_idx, val) in enumerate(row, 1):
                # update trace
                if row_idx == col_idx:
                    k += val

                # update seen set
                col_seen[col_idx].add(val)
                row_seen[row_idx].add(val)

        r = 0
        for row_vals in row_seen.values():
            r += len(row_vals) != N

        c = 0
        for col_vals in col_seen.values():
            c += len(col_vals) != N

        # k: the trace of the matrix
        # r: the number of rows of the matrix that contain repeated elements
        # c: the number of columns of the matrix that contain repeated elements.
        print("Case #{x}: {k} {r} {c}".format(x=x, k=k, r=r, c=c))


if __name__ == '__main__':
    main()