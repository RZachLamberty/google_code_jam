class DanceFloor():
    def __init__(self, dancers):
        self.dancers = dancers
        self.R = max([r for (r, c) in dancers])
        self.C = max([c for (r, c) in dancers])

    def get_total_interest(self):
        ti = self.interest
        while True:
            anyone_eliminated = self.do_round()
            if not anyone_eliminated:
                return ti
            ti += self.interest

    @property
    def interest(self):
        return sum(self.dancers.values())

    def do_round(self):
        to_eliminate = set()
        for ((i, j), v) in self.dancers.items():
            vn_sum = 0
            vn_ct = 0
            for (i2, j2) in self.neighbors(i, j):
                vn_sum += self.dancers[i2, j2]
                vn_ct += 1
            if vn_ct == 0:
                continue

            vn_avg = float(vn_sum) / vn_ct
            if v < vn_avg:
                to_eliminate.add((i, j))

        for (i, j) in to_eliminate:
            del self.dancers[i, j]

        return to_eliminate

    def neighbors(self, i, j):
        neighbors = []
        # up
        for i1 in range(i - 1, -1, -1):
            if (i1, j) in self.dancers:
                neighbors.append((i1, j))
                break
        # down
        for i1 in range(i + 1, self.R + 1):
            if (i1, j) in self.dancers:
                neighbors.append((i1, j))
                break
        # left
        for j1 in range(j - 1, -1, -1):
            if (i, j1) in self.dancers:
                neighbors.append((i, j1))
                break
        # right
        for j1 in range(j + 1, self.C + 1):
            if (i, j1) in self.dancers:
                neighbors.append((i, j1))
                break

        return neighbors


def main():
    T = int(input())

    for x in range(1, T + 1):
        R, C = [int(_) for _ in input().split(' ')]

        dancers = {}
        for r in range(R):
            for (c, v) in enumerate(input().split(' ')):
                dancers[r, c] = int(v)

        df = DanceFloor(dancers)
        y = df.get_total_interest()

        print("Case #{x}: {y}".format(x=x, y=y))


if __name__ == '__main__':
    # 1
    # 1 3
    # 3 1 2
    main()
