from collections import deque as Queue
# class Problems :
#     def sumOfEachSlidingWindow(self, arr, k):
#         if arr is None or len(arr) == 0 :
#             return None
#
#         queue = Queue()
#         sum = 0
#         result = []
#         for i in arr :
#             if queue.qsize() == k :
#                 element = queue.get(i)
#                 sum -= element
#             queue.put(i)
#             sum += i
#
#             if queue.qsize() == k :
#                 result.append(sum)
#         return result
class Price :
    def __init__(self, price, day):
        self.price = price
        self.day = day

class StockPrice :
    def __init__(self, window=3):
        self.window = window
        self.queue = Queue()


    def addPrice(self, price, day):
        while len(self.queue) > 0 and abs(day - self.queue[-1].day) >= self.window:
            self.queue.pop()
        self.queue.append(Price(price,day))
        print(self.getMax(),self.queue)

    def getMax(self):
        maximum = float('-inf')
        for i in self.queue :
            maximum = max(i.price,maximum)
        return maximum




# print(Problems().sumOfEachSlidingWindow([1,4,3,2,5],3))
stock = StockPrice()
stock.addPrice(1,2)
stock.addPrice(4,4)
stock.addPrice(3,7)
stock.addPrice(2,9)
stock.addPrice(5,11)
