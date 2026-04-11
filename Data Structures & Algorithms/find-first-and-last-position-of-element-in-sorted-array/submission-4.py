from typing import List


class Solution:
   def searchRange(self, nums: List[int], target: int) -> List[int]:
      
       def first_occurrence():
           l, r = 0, len(nums)
           while l < r:
               mid = (l + r) // 2
               if target <= nums[mid]:
                   r = mid
               else:
                   l = mid + 1
           return l if l < len(nums) and nums[l] == target else -1


       def last_occurrence():
           l, r = 0, len(nums)
           while l < r:
               mid = (l + r) // 2
               if target < nums[mid]:
                   r = mid
               else:
                   l = mid + 1
           return l - 1 if l > 0 and nums[l - 1] == target else -1


       return [first_occurrence(), last_occurrence()]
