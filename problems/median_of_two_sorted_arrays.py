"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        len1 = len(nums1)
        len2 = len(nums2)

        p1 = 0
        p2 = 0

        while p1 != len1 and p2 != len2 :
            i1 = nums1[p1]
            i2 = nums2[p2]

            if i1 < i2:
                merged.append(i1)
                p1 += 1
            elif i1 > i2:
                merged.append(i2)
                p2 += 1
            else:
                merged.append(i1)
                merged.append(i1)
                p1 += 1
                p2 += 1

            
        
        if p1 != len1:
            merged.extend(nums1[p1:])

        if p2 != len2:
            merged.extend(nums2[p2:])

        merged_len = len(merged)

        import math
        if merged_len % 2 != 0:
            floor = math.floor(merged_len / 2)
            return merged[floor]
        else:
            ceil = int(merged_len / 2)
            floor = ceil - 1
            return (merged[floor] + merged[ceil]) / 2
