# __Big O Time__
# 

# __Space Complexity__
# 

def isAnagram(s, t):
  if len(s) != len(t):
    return False

  s_letter_count = {}
  t_letter_count = {}

  for i in range(len(s)):
    if s[i] in s_letter_count:
      s_letter_count[s[i]] += 1
    else:
      s_letter_count[s[i]] = 1
    
    if t[i] in t_letter_count:
      t_letter_count[t[i]] += 1
    else:
      t_letter_count[t[i]] = 1

  return t_letter_count == s_letter_count


if __name__ == "__main__":
  print(isAnagram("anagram", "nagaraam"))