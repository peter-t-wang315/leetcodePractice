# __Big O time__
# The Big 0 time would be O(logn) where n is the size of n(numbers 1 to n). This is because we are cutting down the list by half each time we iterate through. This
# leads to n/(2^n). This is also just a binary search function

# __Space complexity__
# This algorithms space complexity is O(1). This is because we always only have 3 new variables that are not dependent on the size of n.


def guess(guessed_num):
    if actual == guessed_num:
        return 0
    if actual > guessed_num:
        return 1
    if actual < guessed_num:
        return -1
    

def guessNumber(n):
    middle = n
    left = 1
    right = n
    while(left < right):
        higher_lower = guess(middle)
        # Guess was higher
        if higher_lower == -1:
            right = middle
        # Guess was lower
        elif higher_lower == 1:
            left = middle
        else:
            return middle
        middle = (right+left)//2
    
    return right


if __name__ == "__main__":
    global actual
    actual = 1
    print(guessNumber(1))