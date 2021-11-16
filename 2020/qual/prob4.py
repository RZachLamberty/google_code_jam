import sys


def query(i, qry_ctr):
    print(i)
    sys.stdout.flush()

    response = input()
    qry_ctr += 1
    try:
        return bool(int(response)), qry_ctr
    except ValueError:
        return response, qry_ctr


SYMMETRIC = True
ANTI_SYMMETRIC = False
UNKNOWN = None


class BitQuerier():
    def __init__(self, B):
        self.B = B
        self.bits = {i: UNKNOWN for i in range(1, self.B + 1)}
        self.symmetry = {i: UNKNOWN for i in range(1, self.B + 1)}

    @property
    def any_unknown(self):
        return UNKNOWN in self.bits.values()

    def get_unknown(self):
        return min(k for (k, v) in self.bits.items() if v is UNKNOWN)

    @property
    def symmetry_types(self):
        return {v for v in self.symmetry.values() if v is not UNKNOWN}

    def get_symmetry_class(self, sym_class=SYMMETRIC):
        return {k for (k, v) in self.symmetry.items() if v is sym_class}

    def get_symmetry_class_repr(self, sym_class=SYMMETRIC):
        i = min(self.get_symmetry_class(sym_class))
        v = self.bits[i]
        assert v is not UNKNOWN
        return i, v

    def flip_symmetry_class(self, sym_class=SYMMETRIC):
        i_to_flip = self.get_symmetry_class(sym_class)
        for i in i_to_flip:
            curr_val = self.bits[i]
            assert curr_val is not UNKNOWN
            self.bits[i] = not curr_val

    @property
    def answer(self):
        lookup = {True: '1', False: '0', UNKNOWN: '?'}
        return ''.join([lookup[self.bits[i]] for i in range(1, self.B + 1)])


def main():
    T, B = [int(_) for _ in input().split()]

    for test_idx in range(T):
        bc = BitQuerier(B)

        # break everything up in sets of 10
        for i in range(15):
            qry_ctr = 0

            # symmetric and anti-symmetric pairs all update the same way. we
            # don't need to figure out what happened, we just now that if one
            # (anti)symmetric pair flipped, all did
            for sym_class in bc.symmetry_types:
                i_prev, v_prev = bc.get_symmetry_class_repr(sym_class)
                v_new, qry_ctr = query(i_prev, qry_ctr)

                if v_new != v_prev:
                    bc.flip_symmetry_class(sym_class)

            # if we only queried once, just burn a query (have to to keep pair
            # queries balanced below
            if qry_ctr == 1:
                _, qry_ctr = query(1, qry_ctr)

            # with whatever is left of our 10 queries, gather data
            while (qry_ctr < 10) and bc.any_unknown:
                i_left = bc.get_unknown()
                i_right = B - i_left + 1
                v_left, qry_ctr = query(i_left, qry_ctr)
                v_right, qry_ctr = query(i_right, qry_ctr)

                bc.bits[i_left] = v_left
                bc.bits[i_right] = v_right

                bc.symmetry[i_left] = bc.symmetry[i_right] = (
                    SYMMETRIC if v_left == v_right else ANTI_SYMMETRIC)

            # two reasons to escape the above loop: we know everything or we
            # are about to hit an update.
            if not bc.any_unknown:
                # finish this test
                break

        result, _ = query(bc.answer, 0)
        if result == 'N':
            exit()
        elif result == 'Y':
            continue
        else:
            raise ValueError('how did we get result {}'.format(result))


if __name__ == '__main__':
    main()
