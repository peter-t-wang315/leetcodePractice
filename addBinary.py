def addBinary(str1, str2):
    sum = 0
    finalStr = ""
    length = max(len(str1), len(str2))
    num1 = int(str1)
    num2 = int(str2)
    for i in range(length):
        if i < len(str1):
            sum += (num1%10) * (2**i)
            num1 //= 10
        if i < len(str2):
            sum += (num2%10) * (2**i)
            num2 //= 10
    
    for i in range(length+1):
        if sum - (2**(length-i)) >= 0:
            sum -= 2**(length-i)
            finalStr = finalStr + "1"
        else:
            if i != 0:
                finalStr = finalStr +"0"

    return finalStr

if __name__ == "__main__":
    print(addBinary("10", "1"))