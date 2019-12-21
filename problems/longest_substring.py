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
        max_length_so_far = start = 0

        dict = {}

        for index,value in enumerate(s):
            if value in dict:
                temp_start = dict[value] + 1

                # only move pointer right
                if temp_start > start:
                    start = temp_start

            max_length_so_far = max(max_length_so_far, index + 1 - start)
            dict[value] = index
    
        return max_length_so_far

"""
Version 2:
Only need to loop the entire array once and use less variables to track
Tricky part is the start pointer should always move right

each time in the loop,
* we compare if current value is duplicate or not. 
*   if so:
      we get the position of its next char. If it is smaller than our current start value, we skip it as we know there is duplicate already before the current start
    otherwise:
      update start

"""
