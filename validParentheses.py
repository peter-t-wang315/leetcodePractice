# __Big O time__
# The big O time of this algorithm would be O(n) where n is the size of the string given. This is because we iterate through the entire string once. This time complexity
# is very good for a question like this as to check for valid parentheses, you have to go through each character at least once to know if they create valid parentheses.

# __Space complexity__
# The space complexity of this algorithm would be O(n) where n is the size of the string given. This is because as we iterate through the entire string, we are storing
# each character at least once into the stack of characters. The space complexity for this could be improved to constant space but at the cost of time complexity. Because
# of this I believe that this space complexity is acceptable.

def isValid(s):
    stackCharacters = []

    for i in s:
        if not stackCharacters and (i == ")" or i == "]" or i == "}"): # If there is nothing in the stackCharacters and we find a closing bracket.
            return False
        if i == ")":
            if stackCharacters[-1] != "(":
                return False
            stackCharacters.pop()
        elif i == "]":
            if stackCharacters[-1] != "[":
                return False
            stackCharacters.pop()
        elif i == "}":
            if stackCharacters[-1] != "{":
                return False
            stackCharacters.pop()
        else:
            stackCharacters.append(i)
    if stackCharacters:
        return False
    return True


if __name__ == "__main__":
    print(isValid("()"))