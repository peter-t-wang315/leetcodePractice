# __Initial thoughts__
# Edge cases: 
#   Negative nums
#   Switching an existing 2 nums around? Or just replacing? Ans: Changing, not switching
# Initial ideas:
#   Problems is switching the middle of a number
#   Convert to string and switch that way
#   If the number is negative, change the greatest 9 to a 6
#   If the number is positive, change the greatest 6 to a 9

# __Big O time__
# The Big O time complexity would be O(n) and exact O time being O(2n) where n is the amount of numbers in num. This is because it would
# need to first iterate over num when I changed it to a string for stringNum = str(num), then again when I enumerated through the entire
# stringNum.

# __Space complexity__
# The space complexity of this would be O(n) or exactly O(2n) where n is the amount of numbers in num. This is because I first copy num as
# string into stringNum, then I create another number that will be the same length as num. 

def maximum69Number(num):
    if num < 0:
        targetNum = '9'
        replaceNum = 6
        num*=-1
    else:
        targetNum = '6'
        replaceNum = 9
    stringNum = str(num)
    newNum = 0
    alreadyReplacedFlag = False

    for i, val in enumerate(stringNum):
        newNum*=10
        if alreadyReplacedFlag == False and val == targetNum:
            newNum += replaceNum
            alreadyReplacedFlag = True
        else:
            newNum+=int(val)
    
    return newNum
    

if __name__ == "__main__":
    print(maximum69Number(-6696))