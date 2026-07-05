Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = self.prev = None
        self.freq = 1
class DLL:
    def __init__(self):
        self.head,self.tail = Node(-1,-1),Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def add_node(self,node):
        prev,nxt = self.tail.prev,self.tail
        prev.next,nxt.prev = node,node
        node.next = nxt
        node.prev = prev
        self.size += 1
    def remove_node(self,node):
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
    def pop(self):
        node = self.head.next
        self.remove_node(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.cache = defaultdict(DLL)
        self.freq_node = {}
        self.mn = 1
    def get(self, key: int) -> int:
        if key in self.freq_node:
            node = self.freq_node[key]
            freq = node.freq
            self.cache[freq].remove_node(node)
            if self.cache[freq].size == 0:
                if self.mn == freq:
                    self.mn = freq + 1
                del self.cache[freq]
            node.freq += 1
            self.cache[freq + 1].add_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.freq_node:
            node = self.freq_node[key]
            freq = node.freq
            self.cache[freq].remove_node(node)
            if self.cache[freq].size == 0:
                if self.mn == freq:
                    self.mn = freq + 1
                del self.cache[freq]
            node.freq += 1
            node.val = value
            self.cache[freq + 1].add_node(node)
            return 
        if self.count == self.cap:
            lfu = self.cache[self.mn].pop()
            del_key = lfu.key
            del self.freq_node[del_key]
            self.count -= 1
        node = Node(key,value)
        self.mn = 1
        self.cache[1].add_node(node)
        self.freq_node[key] = node
        self.count += 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
