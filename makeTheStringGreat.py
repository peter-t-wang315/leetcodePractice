# __Big O time__
# The Big O time complexity is O(n) where n is the length of the string. That is because at most, each character is traveresed twice.
# __Space complexity__
# The space complexity is O(n) where n is the length of the string. That is because it is replacing the given string with a new string
# which makes it O(n).


def makeGood(s):
    size = len(s)-1
    i = 0
    while i < size:
        if s[i].lower() == s[i+1].lower() and ((s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower())):
            s = s.replace(s[i:i+2], "", 1)
            size-=2
            i-=1
        else:
            i+=1
    return s

if __name__ == "__main__":
    print(makeGood("NAanorRoOrROwnTNW"))
        
            

