def valid_phone_number(input):
    num_count=0
    for current in input:
        if num_count > 10:
            return False
        if current.isdigit():
            num_count+=1
    
    if num_count == 10:
        return True
    return False


if __name__ == "__main__":
    print(valid_phone_number("23445734562"))

# Fastest big O(n) because no matter what you will have to check each character to determine if there are integers inbetween. Could be constant time if there are enough
# cores to support threading. Where each core checks one character simultaneously