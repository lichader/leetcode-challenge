"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)

        if string_length == 0:
            return 0

        for length in reversed(range(2, string_length+1)):
            for start in range(string_length - length + 1):
                end = start + length
                sub_string = s[start:end]

                unique_chars = set(list(sub_string))
                if len(unique_chars) == length:
                    return length

        return 1
