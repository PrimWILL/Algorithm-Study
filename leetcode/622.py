class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = list()
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if len(self.cq) < self.limit:
            self.cq.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            del self.cq[0]
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.cq[0]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.cq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.cq

    def isFull(self) -> bool:
        return len(self.cq) == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()