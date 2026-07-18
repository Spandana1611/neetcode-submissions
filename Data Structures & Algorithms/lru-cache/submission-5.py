
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(int)
        self.keys_order = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # print('get', self.keys_order, key)
        v = self.cache[key]
        if v!=0:
            self.keys_order.remove(key)
            self.keys_order.append(key)
        # print('get', self.keys_order, key)
        return v - 1

    def put(self, key: int, value: int) -> None:
        # print('put', self.keys_order, key, len(self.keys_order))
        # print(self.cache)
        if key in self.keys_order:
            self.cache[key] = value+1
            self.keys_order.remove(key)
            self.keys_order.append(key)
        elif len(self.keys_order) == self.capacity:
            del self.cache[self.keys_order[0]]
            self.keys_order = self.keys_order[1:]
            self.keys_order.append(key)
            self.cache[key] = value+1
        else:
            self.keys_order.append(key)
            self.cache[key] = value+1
        # print('put', self.keys_order, self.cache)
        # print('done')
