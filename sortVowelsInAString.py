# __Big O Time__
# The big O time complexity of this algorithm is O(n) where n is the size of the input string. This is because we iterate over the string only twice. The use of the index function in the first for loop 
# is deceiving in that it is iterating over a constant sized list which maintains the O(n) time. This is a good time complexity as the entire string must be iterated on to find all of the vowels.

# __Space Complexity__
# The space complexity of this algorithm is O(n) where n is the size of the input string. This is because the algorithm creates an output string which is the same size as the input string. This is a good
# space complexity since strings are immutable, a new string must be created to be able to return.

def sortVowels(str):
    vowels = [0,0,0,0,0,0,0,0,0,0]
    vowelOrder = "AEIOUaeiou"
    vowelIndex = 0
    output = ""
    for letter in str:
        if letter in vowelOrder:
            vowels[vowelOrder.index(letter)] += 1

    for index, letter in enumerate(str):
        if letter in vowelOrder:
            if vowels[vowelIndex] != 0:
                vowels[vowelIndex] -= 1
                output += vowelOrder[vowelIndex]
            else:
                while vowels[vowelIndex] == 0:
                    vowelIndex += 1
                vowels[vowelIndex] -= 1
                output += vowelOrder[vowelIndex]
        else:
            output += str[index]

    return output


if __name__ == "__main__":
    print(sortVowels("lEetcOde"))