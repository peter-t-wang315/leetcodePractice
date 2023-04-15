# __Big O Time__
# The big O time complexity of this algorithm is O(n) where n is the size of the string. This is because the string s
# is iterated over at most twice where its being iterated over once and then the output stack is iterated over which is
# just at most s. This is a reasonable time complexity as each character had to have been iterated over at least once.

# __Space Complexity__
# The space complexity of this algorithm is O(n) where n is the size of the input string. This is because we create 
# basically a copy of S. This is a reasonable space complexity as it makes for a very simple algorithm and helps to
# keep time complexity lower.

def removeStars(s):
    output = []
    for char in s:
        if char == "*":
            output.pop()
        else:
            output.append(char)
    return "".join(output)

if __name__ == "__main__":
    print(removeStars("leet**cod*e"))