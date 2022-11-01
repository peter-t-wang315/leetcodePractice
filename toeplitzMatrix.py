def isToeplitzMatrix(matrix):
    if len(matrix) <= 1:
        return True

    for row in range(len(matrix)-1):
        for col in range(len(matrix[0])-1):
            if matrix[row][col] != matrix[row+1][col+1]:
                return False
    return True    


if __name__ == '__main__':
    print(isToeplitzMatrix([[1,2,3,4,6], [5,1,2,3,4], [9,5,1,3,3], [8,9,5,1,2]]))


