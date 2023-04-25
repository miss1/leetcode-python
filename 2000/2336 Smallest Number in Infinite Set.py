class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.add_back = set()
        self.h = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.h):
            res = heapq.heappop(self.h)
            self.add_back.remove(res)
        else:
            res = self.current
            self.current += 1
        return res

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.current <= num or num in self.add_back:
            return
        heapq.heappush(self.h, num)
        self.add_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)