# __Big O time__
# The big O time complexity for this algorithm is O(nm) where n is the length of "strs" and m is the length of the strings in side of "strs". This is because we have to 
# go through every letter of the strings inside of "strs" n amount of times. 

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because no matter what we only create 1 variable. This is the best space complexity as constant space is the
# most optimal.

def minDeletionSize(strs):
    count = 0
    for index in range(len(strs[0])):
        for wordIndex in range(len(strs)-1):
            if strs[wordIndex][index] > strs[wordIndex+1][index]:
                count += 1
                break
    return count

if __name__ == "__main__":
    print(minDeletionSize(["zyx","wvu","tsr"]))