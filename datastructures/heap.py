class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:  # достижение вершины кучи
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def __str__(self):
        res = []
        start = 0
        end = 1
        n = 1
        while True:
            if not self.heap_list[start:end]:
                break

            res.append('\n')
            res.extend(map(str, self.heap_list[start:end]))
            start, end = end, end + 2 ** n
            n += 1

        return ''.join(res)


bh = BinHeap()
bh.insert(2)
bh.insert(1)
bh.insert(7)
bh.insert(6)
bh.insert(3)
bh.insert(4)
bh.insert(5)
print(bh)
