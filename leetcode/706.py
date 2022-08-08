class MyHashMap:

    def __init__(self):
        self.hashMap = list()

    def put(self, key: int, value: int) -> None:
        for i, x in enumerate(self.hashMap):
            if x[0] == key:
                x[1] = value
                return None
        self.hashMap.append([key, value])
        return None

    def get(self, key: int) -> int:
        for k, v in self.hashMap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, x in enumerate(self.hashMap):
            if x[0] == key:
                del self.hashMap[i] 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
