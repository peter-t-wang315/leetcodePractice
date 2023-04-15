def miniMaxSum(arr):
    arr.sort()
    print(arr[0]+arr[1]+arr[2]+arr[3], arr[1]+arr[2]+arr[3]+arr[4])

if __name__ == "__main__":
    print(miniMaxSum([1,2,3,4,5]))