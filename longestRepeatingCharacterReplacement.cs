using System;

public class Solution
{
    public static void Main()
    {
        Solution sol = new Solution();
        string s = "AABABBA";
        int k = 1;
        int result = sol.CharacterReplacement(s, k);
        Console.WriteLine(result);
    }

    public int CharacterReplacement(string s, int k)
    {
        int longestRepeating = 0;
        int replaced;
        char startingChar;
        int secondIndex = 0;

        for (int i = 0; i < s.Length; i++)
        {
            replaced = 0;
            startingChar = s[i];

            for (secondIndex = 0; replaced <= k && secondIndex + i < s.Length; secondIndex++)
            {
                if (s[secondIndex + i] != startingChar)
                {
                    if (replaced == k) break;
                    replaced++;
                }
            }

            longestRepeating = Math.Max(longestRepeating, secondIndex);
        }

        return longestRepeating;
    }
}
