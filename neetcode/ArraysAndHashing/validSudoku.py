# Holy cow I got this basically first try. I typoed and put a >2 on the squareCount check instead of >1 so it messed up there. But other than that first try.

# __Big O Time__
# O(1). This is because board is a constant 81 size. Meaning that it is constant and can be reduced to 1.

# __Space Complexity__
# O(1). This is because my used space is also a constant size as my inputs don't rely on input sizes.

def isValidSudoku(board):
    squareCount = {0: {0: [0]*9, 1: [0]*9, 2: [0]*9}, 1: {0: [0]*9, 1: [0]*9, 2: [0]*9}, 2: {0: [0]*9, 1: [0]*9, 2: [0]*9}}
    columnCount = {0: [0]*9, 1: [0]*9, 2:[0]*9, 3:[0]*9, 4:[0]*9, 5:[0]*9, 6:[0]*9, 7:[0]*9, 8:[0]*9}

    for rowIndex, column in enumerate(board):
        # Make a blank currentRowCount to see if duplicate numbers exist in a row
        currentRowCount = [0]*9
        # Iterate over every row item
        for columnIndex, rowItem in enumerate(column):
            if rowItem != ".":
                # Make rowItem fit
                rowItem = int(rowItem) - 1
                # Check if a number has appeared more than once in a row
                currentRowCount[rowItem] += 1
                if currentRowCount[rowItem] > 1:
                    return False
                
                # Add to it's appropriate column
                columnCount[columnIndex][rowItem] += 1
                if columnCount[columnIndex][rowItem] > 1:
                    return False

                # Add to it's appropriate square
                squareCount[rowIndex // 3][columnIndex // 3][rowItem] += 1
                if squareCount[rowIndex // 3][columnIndex // 3][rowItem] > 1:
                    return False
    
    return True
            
            

if __name__ == "__main__":
    print(isValidSudoku([
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]))