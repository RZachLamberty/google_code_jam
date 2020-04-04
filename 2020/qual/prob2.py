def main():
    T = int(input())

    for x in range(1, T + 1):
        S = [int(_) for _ in input()]

        # print(f'\n\nstarting case #{x}')  # rm
        # print(f'S = {S}')  # rm

        y = ''
        closure_depth = 0

        # keep y closed. for each new value, if it fits within the previous
        # closed y, move it in. otherwise add a new element
        for next_val in S:
            # print(f'\ny = {y}') # rm
            # print(f'closure_depth = {closure_depth}') # rm
            # print(f'next_val = {next_val}') # rm
            if next_val == 0:
                y += str(next_val)
                closure_depth = 0
            elif next_val > closure_depth:
                for i in range(next_val):
                    y += '('
                y += str(next_val)
                for i in range(next_val):
                    y += ')'
                closure_depth = next_val
            else:
                # walk backwards through y until we are next_val parens deep
                # if we hit another number, we can add the remaining closure
                # depth around just our chosen number
                depth = 0
                for (i, c) in enumerate(reversed(y), 1):
                    if c == ')':
                        depth += 1
                    elif c == '(':
                        depth -= 1
                    else:
                        additional_parens_needed = next_val - depth
                        y = (y[:-depth]
                             + ('(' * additional_parens_needed)
                             + str(next_val)
                             + (')' * additional_parens_needed)
                             + y[-depth:])
                        break

                    if depth == next_val:
                        y = y[:-depth] + str(next_val) + y[-depth:]
                        break
            # print(f'new y = {y}')  # rm

        # x: the test case number (starting from 1)
        # y: the string S' defined above.
        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    main()