class LRULink_node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # init capacity
        self.capacity = capacity
        self.size = 0
        # init head and tail node
        self.head = LRULink_node()
        self.tail = LRULink_node()
        self.head.next = self.tail
        self.tail.pre = self.head
        # init hash map dict
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key not in self.hash_map: return -1
        key_node = self.hash_map[key]
        self.remove_cache(key_node)
        self.insert_cacahe(self.head, key_node)
        return key_node.value

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:
            self.hash_map[key].value = value
            self.remove_cache(self.hash_map[key])
            self.insert_cacahe(self.head, self.hash_map[key])
        else:
            key_node = LRULink_node(key, value)
            self.hash_map[key] = key_node
            self.insert_cacahe(self.head, key_node)
            self.size += 1
            if self.size > self.capacity:
                self.hash_map.pop(self.tail.pre.key)
                self.remove_cache(self.tail.pre)
                self.size -= 1

    def remove_cache(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insert_cacahe(self, node_head, node):
        node_head.next.pre = node
        node.next = node_head.next

        node.pre = node_head
        node_head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
