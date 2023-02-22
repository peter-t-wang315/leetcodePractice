def findAnagrams(s, p):
    len_substring = len(p)
    letter_count_in_substring = {}
    output = []
    for character in p:
        if letter_count_in_substring.get(character):
            letter_count_in_substring[character]+=1
        else:
            letter_count_in_substring[character] = 1

    for i in range(len(s)-len_substring+1):
        current_substring = s[i:i+len_substring]
        if isAnagram(letter_count_in_substring, current_substring):
            output.append(i)

    return output

def isAnagram(letter_count_in_substring, substring):
    for letter in letter_count_in_substring.keys():
            if letter_count_in_substring[letter] != substring.count(letter):
                return False
    return True


if __name__ == '__main__':
    print(findAnagrams("cbaebabacd", "abc"))
