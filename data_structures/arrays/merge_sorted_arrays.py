# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        insert = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 -= 1
                insert -= 1
            else:
                nums1[insert] = nums2[p2]
                p2 -= 1
                insert -= 1

        #incase p2 is still left
        while p2 >= 0:
            nums1[insert] = nums2[p2]
            p2 -= 1
            insert -= 1

        return nums1

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(s.merge(nums1, m, nums2, n))

