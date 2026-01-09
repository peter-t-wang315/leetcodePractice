// __Big O Time__ 
// The big O time of this algorithm is O(n) where n is the size of the string passed in. This is because we at most go through the string twice but O(2n) goes to O(n).

// __Space complexity__
// The space complexity of this algorithm is O(1). This is because you only need to create 2 ints which are constant space.


public class Solution {
    public bool ValidPalindrome(string s) {
        int lPtr = 0;
        // Account for 0 based indexing;
        int rPtr = s.Length-1;

        while (lPtr < rPtr) {
            // If the palindrome is palindroming, just keep going.
            if (s[lPtr] == s[rPtr]) {
                lPtr++;
                rPtr--;
            }

            else {
                if (isPalindrome(s, lPtr+1, rPtr) || isPalindrome(s, lPtr, rPtr-1)) {
                    return true;
                }
                else {
                    return false;
                }
            }
        }

        return true;
    }

    public bool isPalindrome(string s, int lPtr, int rPtr) {
        while (lPtr < rPtr) {
            if (s[lPtr] != s[rPtr]) {
                return false;
            }
            lPtr++;
            rPtr--;
        }
        return true;
    }
}