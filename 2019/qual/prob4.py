# N: number of worker computers
# B: number of broken workers
# F: number of calls allowed
# T: number of test cases to solve

import math
import sys


def parse_test_case():
    return [int(_) for _ in input().split(' ')]


UNKNOWN = '?'
BROKEN = ' '
WORKING = '+'


class Segment:
    def __init__(self, l, b):
        self.b = b
        self.l = l

    def __repr__(self):
        return '<{}|{}>'.format(''.join(self.l), self.b)

    def __len__(self):
        return len(self.l)

    @property
    def n(self):
        return len(self)

    def num_lft_rt(self):
        L = len(self)
        halfway = math.ceil(L / 2)
        return halfway, L - halfway

    def split(self):
        lft, rt = self.num_lft_rt()
        return [self.l[:lft], self.l[lft:]]

    def guess(self):
        if self.solved:
            return '0' * len(self)
        else:
            lft, rt = self.num_lft_rt()
            return '0' * lft + '1' * rt

    @property
    def solved(self):
        return not any([_ == UNKNOWN for _ in self.l])


def solve(N, B, F):
    machine_status = [Segment([UNKNOWN for i in range(N)], B)]
    for i in range(F):
        # construct a guess from the existing segments
        guess = ''.join([s.guess() for s in machine_status])

        print(guess)
        sys.stdout.flush()

        guess_response = input()

        # parse the response segment-by-segment
        # each segment is expecting n - b elements returned
        new_machine_status = []
        for (j, segment) in enumerate(machine_status):
            n = segment.n - segment.b
            seg_response = guess_response[:n]
            guess_response = guess_response[n:]

            if segment.solved:
                # we guessed segment.n 0s, and should have received
                # segment.n - segment.b 0s
                assert seg_response == '0' * n
                new_machine_status.append(segment)

            else:
                num_lft = seg_response.count('0')
                num_rt = seg_response.count('1')
                expected_lft, expected_rt = segment.num_lft_rt()
                b_lft = expected_lft - num_lft
                b_rt = expected_rt - num_rt

                # if b_lft or b_rt = 0, all items in the left (right) are
                # working
                l_lft, l_rt = segment.split()
                if b_lft == 0:
                    l_lft = [WORKING for _ in range(len(l_lft))]
                elif b_lft == expected_lft:
                    l_lft = [BROKEN for _ in range(len(l_lft))]

                if b_rt == 0:
                    l_rt = [WORKING for _ in range(len(l_rt))]
                elif b_rt == expected_rt:
                    l_rt = [BROKEN for _ in range(len(l_rt))]

                new_machine_status.append(Segment(l_lft, b_lft))
                new_machine_status.append(Segment(l_rt, b_rt))

        # check if all segments are finished
        if all([_.solved for _ in new_machine_status]):
            flat = [elem
                    for segment in new_machine_status
                    for elem in segment.l]
            broken_ones = [i
                           for (i, elem) in enumerate(flat)
                           if elem == BROKEN]
            print(' '.join([str(_) for _ in broken_ones]))
            sys.stdout.flush()

            judge_response = input()
            if judge_response == '1':
                return
            else:
                exit(1)

        machine_status = new_machine_status

    exit(1)


def main():
    T = int(input())
    for i_test_case in range(T):
        N, B, F = parse_test_case()
        solve(N, B, F)


if __name__ == '__main__':
    main()
