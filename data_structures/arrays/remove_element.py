from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums[i] = '_'
            print(nums)
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] == '_':
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                else:
                    left += 1
            counter = 0
            print(nums)
            while counter < len(nums) and nums[counter] != '_':
                counter += 1

            return counter
s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
s.removeElement(nums, val)