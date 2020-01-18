"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = len(s)

        for sub_length in reversed(range(1, length + 1)):
            for begining in range(length + 1 - sub_length):
                if sub_length % 2 == 0:
                    first_half = begining + sub_length // 2

                    s1 = s[begining:first_half]
                    s2 = s[first_half:(begining+sub_length)][::-1]

                    if s1 == s2:
                        return s[begining:(begining+sub_length)]
                
                else:
                    first_half = begining + sub_length // 2
                    
                    s1 = s[begining:first_half]
                    s2 = s[first_half+1:(begining+sub_length)][::-1]

                    if s1 == s2:
                        return s[begining:(begining+sub_length)]
        
        return ""
