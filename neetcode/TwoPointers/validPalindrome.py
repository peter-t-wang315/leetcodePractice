# __Big O Time__
# O(n) n being the size of the input string

# __Space Complexity__
# O(1) as I have to create 2 constants

def isPalindrome(s):
    leftIndex = 0
    rightIndex = len(s)-1

    while (not (s[leftIndex].isalpha() or s[leftIndex].isdigit())) and leftIndex < len(s)-1:
        leftIndex += 1
        
    while (not (s[rightIndex].isalpha() or s[rightIndex].isdigit())) and rightIndex > 0:
        rightIndex -= 1

    while leftIndex < rightIndex:
        if s[leftIndex].lower() != s[rightIndex].lower():
            return False
        else:
            leftIndex += 1
            rightIndex -= 1

        while not (s[leftIndex].isalpha() or s[leftIndex].isdigit()):
            leftIndex += 1
        
        while not (s[rightIndex].isalpha() or s[rightIndex].isdigit()):
            rightIndex -= 1

    return True

if __name__ == "__main__":
    print(isPalindrome("A."))