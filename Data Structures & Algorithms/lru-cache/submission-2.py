class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.maximum = capacity
        self.size = 0
        # initalize kv_map for mapping keys to values for O(1) get
        self.kv_map = defaultdict(Node)

        # doubly linked list with lru and mru pointers for O(1) put
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)

        self.lru.next, self.mru.prev = self.mru, self.lru

    def get(self, key: int) -> int:
        if key in self.kv_map:
            # move to mru
            node = self.kv_map[key]

            # modify its neighbors pointers to evict it from the position
            node.prev.next = node.next
            node.next.prev = node.prev
            
            # modify mru pointers to make it mru
            node.prev = self.mru.prev
            node.next = self.mru
            self.mru.prev.next = node
            self.mru.prev = node

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        overfill = 0
        # update if key exists
        if key in self.kv_map:
            self.kv_map[key].val = value
            # move to mru
            node = self.kv_map[key]

            # modify its neighbors pointers to evict it from the position
            node.prev.next = node.next
            node.next.prev = node.prev
            
            # modify mru pointers to make it mru
            node.prev = self.mru.prev
            node.next = self.mru
            self.mru.prev.next = node
            self.mru.prev = node
            return
        
        # if trying to overfill, evict lru
        if self.size >= self.maximum:
            old_key = self.lru.next.key
            self.lru.next = self.lru.next.next
            self.lru.next.prev = self.lru
            overfill = 1
            del self.kv_map[old_key]
        
        # normal put operation (updates MRU)
        self.kv_map[key] = Node(key, value)
        node = self.kv_map[key]
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev.next = node
        self.mru.prev = node

        if not overfill:
            self.size += 1
        return