from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            left = 0
            right = 1
            while right < len(nums):
               if nums[left] != nums[right]:
                   left += 1
                   right += 1
               else:
                   nums[right] = '_'
                   right += 1
                   left += 1
        left = 0
        right = len(nums) - 1
        while len(nums) > 0 and left < right:
            if nums[left] == '_':
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        print(nums)
        return nums.index('_')

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))


