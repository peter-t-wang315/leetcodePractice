def timeConversion(s):
    output = ""
    if s[-2:] == "AM":
        if s[:2] == "12":
            output = "00"+s[2:-2]
        else:
            output = s[:-2]
    else:
        if s[:2] != "12":
            new_hour = int(s[:2])+12
            output = str(new_hour)+s[2:-2]
        else:
            output = s[:-2]

    return output



if __name__ == "__main__":
    print(timeConversion("12:01:00PM"))