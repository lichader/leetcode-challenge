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


"""
We actually only need to iterate half elements of m+n
because we only need to know the value of elements in the middle

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        len1 = len(nums1)
        len2 = len(nums2)

        total_size = len1 + len2

        left = 0
        right = 0

        import math
        if total_size % 2 == 0:
            right = int(total_size / 2)
            left = right - 1
        else:
            right = math.floor(total_size / 2)
            left = right

        p1 = 0
        p2 = 0

        while len(merged) < (right + 1) :
            i1 = None
            i2 = None

            if p1 < len1:
                i1 = nums1[p1]

            if p2 < len2:
                i2 = nums2[p2]

            if i1 != None and i2 != None:
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
            elif i1 != None:
                merged.append(i1)
                p1 += 1
            elif i2 != None:
                merged.append(i2)
                p2 += 1

        return (merged[left] + merged[right]) / 2
            
