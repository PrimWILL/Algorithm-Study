class MyHashMap:

    def __init__(self):
        self.hashMap = list()

    def put(self, key: int, value: int) -> None:
        for i, x in enumerate(self.hashMap):
            if x[0] == key:
                x[1] = value
                return None
        self.hashMap.append([key, value])
        self.hashMap.sort(key = lambda x: x[0])
        return None

    def get(self, key: int) -> int:
        left = 0
        right = len(self.hashMap) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.hashMap[mid][0] == key:
                return self.hashMap[mid][1]
            elif self.hashMap[mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def remove(self, key: int) -> None:
        left = 0
        right = len(self.hashMap) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.hashMap[mid][0] == key:
                del self.hashMap[mid]
                return None
            elif self.hashMap[mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
