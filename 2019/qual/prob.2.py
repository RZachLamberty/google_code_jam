num_test_cases = int(input())

for case_num in range(1, num_test_cases + 1):
    grid_size = int(input())
    lydias_path = input()

    my_path = (lydias_path
               .replace('E', 'r')
               .replace('S', 'E')
               .replace('r', 'S'))

    print("Case #{}: {}".format(case_num, my_path))
