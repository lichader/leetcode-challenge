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
        length = len(s)

        max_length_so_far = start = end = 0

        while (start < length and end < length):
            sub_string = s[start:end]
            next_char = s[end]
            end += 1

            pos = sub_string.find(next_char)
            if pos != -1:
                start = start + pos + 1
            else:
                max_length_so_far = max(max_length_so_far, len(sub_string)+1)
                
            
        return max_length_so_far

"""
Start from index 0, 1 
Search next char: 2 
If next char is in current sub string, take a note of current max and slide to that character
update index: start to the pos + 1 of that character 
and increase j
"""
