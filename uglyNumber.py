# __Big O time__
# The big O time complexity would be O(logn) where n is the size of the input int. The reason being that each iteration we go through we are dividing 
# the number by at least half each time.

# __Space complexity__
# The space complexity of this algorithm is O(1). That is because there is no new memory being used or created.

def isUgly(n):
    if n <= 0:
        return False
    while n > 1:
        if n%2==0:
            n/=2
        elif n%3==0:
            n/=3
        elif n%5==0:
            n/=5
        else:
            return False
    return True
        
    

if __name__ == "__main__":
    print(isUgly(6))