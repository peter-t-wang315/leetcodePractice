def arrayStringsAreEqual(lWord1, lWord2):
    concatWord1 = ""
    concatWord2 = ""
    for i in range(max(len(lWord1), len(lWord2))):
        if i < len(lWord1):
            concatWord1 += lWord1[i]
        if i < len(lWord2):
            concatWord2 += lWord2[i]
    if concatWord1 == concatWord2: # What O(n) would this be?
        return True
    return False


if __name__ == "__main__":
    print(arrayStringsAreEqual(["ab","c"], ["a","bc"]))