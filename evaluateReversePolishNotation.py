# __Big O time__
# The big O time complexity for this algorithm is O(n) where n is the size of the list passed through. This is because we iterate over every element of the list at most two times; one to pop and put it into an
# array, one time to take it out of said array. This is a reasonable time complexity as no matter what, you have to see every element of the list at least one time.

# __Space complexity__
# The space complexity of this algorithm is O(n) where n is the size of the list passed through. This is because we store every single operand at least once. This is a reasonable space complexity because
# to lower space complexity, you would have to sacrifice time complexity.

import math

def evalRPN(tokens):
    if len(tokens) == 1:
        return int(tokens[0])

    numStack = []
    for item in tokens:
        if item == "+":
            numStack.append(numStack.pop() + numStack.pop())
        elif item == "-":
            right = numStack.pop()
            numStack.append(numStack.pop() - right)
        elif item == "*":
            numStack.append(numStack.pop() * numStack.pop())
        elif item == "/":
            right = numStack.pop()
            numStack.append(math.trunc(numStack.pop()/right))
        else:
            numStack.append(int(item))
    
    return numStack[0]


if __name__ == "__main__":
    print(evalRPN(["4","-2","/","2","-3","/","-"]))