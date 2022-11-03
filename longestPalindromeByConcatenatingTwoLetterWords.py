# The Big O time complexity for my algorithm is O(n) where n is the size of the list words. That is because it iterates over every single item in the list.
# Although there is a second for loop, that second for loops largest possible size is only 26 as it holds the the same letter items(aa, ee, gg, etc.). This means
# that the only possible contents in the dictionary are the letters of the alphabet. This constant size means that it is constant time and can be reduced for 
# the Big O time. The space complexity is O(n) as well where n is the number of items in the list.

def longestPalindrome(words):
    different_letters_dict = {}
    same_letters_dict = {}
    count = 0
    for i in range(len(words)):
        if words[i][0] == words[i][1]:
            if same_letters_dict.get(words[i]):
                same_letters_dict[words[i]] +=1
            else:
                same_letters_dict[words[i]] = 1
        else:
            if different_letters_dict.get(words[i][::-1]):
                if different_letters_dict.get(words[i][::-1]) > 0:
                    different_letters_dict[words[i][::-1]] -= 1
                    count+=4
            else:
                if different_letters_dict.get(words[i]):
                    different_letters_dict[words[i]] += 1
                else:
                    different_letters_dict[words[i]] = 1 
    
    middle_of_palindrome_flag = False
    for same_letter in same_letters_dict.keys():
        same_letter_occurences = same_letters_dict.get(same_letter)
        if middle_of_palindrome_flag == False and same_letter_occurences == 1:
            middle_of_palindrome_flag = True
            count += 2
        if same_letter_occurences > 1:
            if same_letter_occurences % 2 == 1:
                count += (same_letter_occurences-1) *2
                if middle_of_palindrome_flag == False:
                    count+=2
                    middle_of_palindrome_flag = True
            else:
                count += same_letter_occurences *2
            
    return count


if __name__ == "__main__":
    print(longestPalindrome(["ab","yy","lc","cl","ba", "yy", "yy", "aa"]))