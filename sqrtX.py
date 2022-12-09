# __Big O complexity__
# The time complexity of this algorithm is O(logn) where n is the size of the number. This is because we are searching for the sqrt(n+1) index making it O(logn). This is
# a reasonable time complexity 

# __Space complexity__
# The space complexity is O(1). This is because we do not create variables based on the inputs. It is always just the int i. This is the best space complexity
# because it cannot be better than constant space.

def mySqrt(x):
    if x == 0:
        return 0
    for i in range(x+1):
        if i*i == x:
            return i
        if i*i > x:
            return i-1
    

if __name__ == "__main__":
    print(mySqrt(145))