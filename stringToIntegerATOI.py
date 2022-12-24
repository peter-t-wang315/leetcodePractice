# __Big O time__
# The big O time complexity of this algorithm is O(n) where n is the length of the input string. This is because my algorithm iterates over every value of input s at most once. This is a reasonable time 
# complexity as to get the integer, one would have to iterate over every index at least once.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because there are only ever 3 things being stored no matter the input. This is the best space complexity as constant space is the best.

def myAtoi(s):
    output = 0
    isNeg = False
    isPos = False
    for char in s:
        if char == '-':
            breakpoint()
            if isPos or isNeg:
                break
            isNeg = True
        elif char == " ":
            if isPos or isNeg:
                break
        elif char == "+":
            if isNeg or isPos:
                break
            isPos = True
        elif char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
            output *= 10
            output += int(char)
            isPos = True
        else:
            break
    if isNeg:
        output *= -1
    if output < -2147483648:
        return -2147483648
    if output > 2147483647:
        return 2147483647
    
    return output


if __name__ == "__main__":
    print(myAtoi("    -88827   5655  U"))