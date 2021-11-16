def decompose_color(c):
    if c == 'U':
        return set()
    elif c in 'RYB':
        return {c,}
    elif c == 'O':
        return {'R', 'Y'}
    elif c == 'P':
        return {'R', 'B'}
    elif c == 'G':
        return {'Y', 'B'}
    else:
        return {'R', 'Y', 'B'}


def main():
    T = int(input())

    for x in range(1, T + 1):
        N = int(input())
        P = input()

        color_sets = [decompose_color(c) for c in P]

        current_strokes = set()
        num_strokes = 0
        for color_set in color_sets:
            strokes_to_stop = set()
            for color in current_strokes:
                if color not in color_set:
                    strokes_to_stop.add(color)
            current_strokes.difference_update(strokes_to_stop)

            strokes_to_start = set()
            for color in color_set:
                if color not in current_strokes:
                    strokes_to_start.add(color)
                    num_strokes += 1
            current_strokes.update(strokes_to_start)

        print(f"Case #{x}: {num_strokes}")


if __name__ == '__main__':
    main()
