import sys

DEBUG = False


def debug(s):
    if DEBUG:
        print(s)


def query(i):
    print(i)
    sys.stdout.flush()

    response = input()
    try:
        return bool(int(response))
    except ValueError:
        return response


def is_reset_query(qry_idx):
    return (qry_idx % 10 == 0) and (qry_idx > 0)


def get_symm_pairs(bit_array, B):
    qry_idx = 0
    i_same = i_diff = None

    for i_left in range(B // 2, 0, -1):
        i_right = B - i_left + 1

        # reset every 10
        if is_reset_query(qry_idx):
            for i in bit_array:
                bit_array[i] = None

        bit_array[i_left] = query(i_left)
        bit_array[i_right] = query(i_right)
        qry_idx += 2

        if (i_same is None) and (bit_array[i_left] == bit_array[i_right]):
            i_same = i_left

        if (i_diff is None) and (bit_array[i_left] != bit_array[i_right]):
            i_diff = i_left

        if i_same and i_diff:
            break

    # leave here with the bit_array values set, hell or high water
    num_to_get = 0
    need_same = (i_same is not None) and bit_array[i_same] is None
    need_diff = (i_diff is not None) and bit_array[i_diff] is None
    if need_same:
        num_to_get += 1
    if need_diff:
        num_to_get += 1

    # make sure we won't trigger a fluctuation between the two
    if num_to_get == 2 and (qry_idx % 10 == 9):
        _ = query(1)
        qry_idx += 1

    if is_reset_query(qry_idx) and num_to_get > 0:
        for i in bit_array:
            bit_array[i] = None

    if need_same:
        i_flip = B - i_same + 1
        bit_array[i_flip] = bit_array[i_same] = query(i_same)
        qry_idx += 1

    if need_diff:
        i_flip = B - i_diff + 1
        bit_array[i_diff] = query(i_diff)
        qry_idx += 1
        bit_array[i_flip] = not bit_array[i_diff]

    return i_same, i_diff, qry_idx


def get_updates(i_same, i_diff, bit_array):
    qry_delta = 0
    if i_same is None:
        # (i_same is None) iff the array is entirely anti-symmetric. this means
        # a bit flip is equivalent to a rotation. this means our four options
        # collapse into only two
        # (  ,  ) --> (  ,  )
        # (BF,  ) --> (BF,  )
        # (  , R) --> (BF,  )
        # (BF, R) --> (  ,  )
        # we can use the diff records to figure out which to choose
        v_diff_prev = bit_array[i_diff]
        v_diff_new = query(i_diff)
        qry_delta += 1
        is_bitflip = v_diff_prev != v_diff_new
        is_reverse = False
    else:
        v_same_prev = bit_array[i_same]
        v_same_new = query(i_same)
        qry_delta += 1
        is_bitflip = (v_same_prev != v_same_new)

        # (i_diff is None) iff the array is entirely symmetric. a reverse is
        # the same as doing nothing
        if i_diff is None:
            is_reverse = False
        else:
            v_diff_prev = bit_array[i_diff]
            v_diff_new = query(i_diff)
            qry_delta += 1
            # enumerate the possibilities, you'll see it's true
            is_reverse = (v_diff_prev == v_diff_new) == is_bitflip

    return is_bitflip, is_reverse, qry_delta


def apply_bitflip(bit_array):
    for (i, v) in bit_array.items():
        if v is not None:
            bit_array[i] = not v


def apply_reverse(bit_array, B):
    return {B - i + 1: v for (i, v) in bit_array.items()}


def bit_array_to_str(bit_array, B):
    lookup = {True: '1', False: '0', None: '?'}
    return ''.join([lookup[bit_array[i]] for i in range(1, B + 1)])


def main():
    T, B = [int(_) for _ in input().split()]

    for test_idx in range(T):
        bit_array = {i: None for i in range(1, B + 1)}

        # get both an equal and opposite symmetric pairs
        i_same, i_diff, qry_idx = get_symm_pairs(bit_array, B)

        is_symmetric = i_diff is None
        is_anti_symmetric = i_same is None

        if is_symmetric and is_anti_symmetric:
            raise ValueError(
                f'found neither i_same nor i_diff for test_idx = {test_idx}')

        yet_unknowns = {k for (k, v) in bit_array.items() if v is None}
        debug(f'yet_unknowns at start: {yet_unknowns}')
        while qry_idx < 150 and yet_unknowns:
            debug(f'qry_idx = {qry_idx}')
            debug(f'bit_array = {bit_array_to_str(bit_array, B)}')
            if is_reset_query(qry_idx):
                is_bitflip, is_reverse, qry_delta = get_updates(i_same, i_diff,
                                                                bit_array)
                if is_bitflip:
                    debug('doing bitflip')
                    apply_bitflip(bit_array)
                if is_reverse:
                    debug('doing reverse')
                    bit_array = apply_reverse(bit_array, B)
                yet_unknowns = {k for (k, v) in bit_array.items() if v is None}
                qry_idx += qry_delta
            else:
                i_q = yet_unknowns.pop()
                bit_array[i_q] = query(i_q)

                i_flip = B - i_q + 1
                if is_symmetric:
                    bit_array[i_flip] = bit_array[i_q]
                    yet_unknowns.discard(i_flip)

                if is_anti_symmetric:
                    bit_array[i_flip] = not bit_array[i_q]
                    yet_unknowns.discard(i_flip)

                qry_idx += 1

        if qry_idx >= 150:
            raise ValueError(f'yup. {bit_array_to_str(bit_array, B)}')
            exit()

        answer = bit_array_to_str(bit_array, B)

        result = query(answer)
        if result == 'N':
            exit()


if __name__ == '__main__':
    main()
