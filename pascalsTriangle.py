# __Big O time__
# The big O time for this algorithm would be O(n^2) where n is the size of list. This is because for each iteration it indexes back to i which then creates the equation
# (n*(n+1))/2 which will simplify back down to O(n^2). This is a reasonable time complexity as to generate each row, you would have to iterate to n each time which 
# again leads to the (n*(n+1))/2 time complexity.

# __Space complexity__
# The space complexity is O(n^2) where n is the size of the list. This is because for each iteration we have to store the (n*(n+1))/2 calculations one to one. This space
# complexity is reasonable because you have to store every single row of the triangle which would take the n^2 space.

def generate(numRows):
    pascalList = []
    for i in range(numRows):
        if i == 0:
            pascalList.append([1])
        elif i == 1:
            pascalList.append([1,1])
        else:
            curRowList = [1]
            for prevRowIndex in range(i-1):
                curRowList.append(pascalList[i-1][prevRowIndex] + pascalList[i-1][prevRowIndex+1])
            curRowList.append(1)
            pascalList.append(curRowList)
    return pascalList
                
        


if __name__ == "__main__":
    print(generate(5))