# __Big O time__
# The big O time complexity of this algorithm in terms of the StockSpanner class is O(n) or specifically O(2n) where n is the amount of `next()`s called.
# Because one item can only be input and taken out of the stack at most two times. 

# __Space complexity__
# The space complexity of this algorithm would be O(n) or specifically O(2n) as well. This is because we are making a list and dictionary of all the inputs given.

class StockSpanner:
    def __init__(self):
        self.stackDays = []
        self.stackLen=0
        self.priceDayDict={}

    def next(self, price: int) -> int:
        if self.stackLen==0 or price < self.stackDays[self.stackLen-1]:
            self.stackDays.append(price)
            self.stackLen+=1
            self.priceDayDict[price]=1
            return 1
        if not self.priceDayDict.get(price):
            self.priceDayDict[price]=0
        while self.stackLen > 0:
            if price < self.stackDays[self.stackLen-1]:
                self.stackDays.append(price)
                self.stackLen+=1
                self.priceDayDict[price]+=1
                return self.priceDayDict[price]
            elif price == self.stackDays[self.stackLen-1]:
                self.priceDayDict[price]+=1
                return self.priceDayDict[price]
            else:
                # Get the most recent day
                prevPrice = self.stackDays.pop()
                # Get the amount of days associated with it
                prevDayCount = self.priceDayDict.get(prevPrice)
                # Add that amount of days to the current days values
                self.priceDayDict[price]+=prevDayCount
                # Delete the day from the dict
                del self.priceDayDict[prevPrice]
                self.stackLen-=1
        self.stackDays.append(price)
        self.stackLen=1
        self.priceDayDict[price] += 1
        return self.priceDayDict[price]
            

if __name__ == "__main__":
    test = StockSpanner()
    while(True):
        line = int(input())
        print("Days consecutive:",test.next(line))
        print("stack:", test.stackDays)
        print("day:", test.stackDays[test.stackLen-1])
        print("dict:",test.priceDayDict)
        print()

        
            