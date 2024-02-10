# __Big O Time__
# O(n) n being the amount of characters in strs

# __Space Complexity__
# O(m) m being the number of strs. This is because I create lists that have the same number of values as strs

def groupAnagrams(strs):
    groupedStrs = {}

    for string in strs:
        # Break the string into a dict
        letterCount = [0]*26
        for char in string:
            letterCount[ord(char.lower())-97] += 1
        
        tupledLetterCount = tuple(letterCount)

        # Check if letterCount exists in the dict already
        if tupledLetterCount in groupedStrs:
            groupedStrs[tupledLetterCount].append(string)
        else:
            groupedStrs[tupledLetterCount] = [string]
    
    return groupedStrs.values()

if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

