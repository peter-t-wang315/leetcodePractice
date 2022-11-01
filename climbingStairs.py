def climbing_stairs_unique_path(amount_stairs): #could also just be num
    if amount_stairs == 1:
        return 1
    if amount_stairs == 2:
        return 2
    s1 = 1
    s2 = 2
    i = 1
    while i < amount_stairs: #for i in range(amount_stairs):
        temp = s2
        s2 = s1+s2
        s1 = temp
        i+=1
    return s1

if __name__ == "__main__":
    print(climbing_stairs_unique_path(5))

# O(n). Fastest because no matter what. Must loop through until the size n to determine the different amount of paths. 