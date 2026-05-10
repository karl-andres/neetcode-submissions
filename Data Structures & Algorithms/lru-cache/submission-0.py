class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.arrlist = []   # [[key, value]] — order matters

    def get(self, key: int) -> int:
        for i in range(len(self.arrlist)):
            if self.arrlist[i][0] == key:
                value = self.arrlist[i][1]
                # move to MRU
                self.arrlist.pop(i)
                self.arrlist.append([key, value])
                return value
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.arrlist)):
            if self.arrlist[i][0] == key:
                # update value + move to MRU
                self.arrlist.pop(i)
                self.arrlist.append([key, value])
                return

        # key not found means insert
        if len(self.arrlist) == self.size:
            self.arrlist.pop(0)  # evict LRU

        self.arrlist.append([key, value])
