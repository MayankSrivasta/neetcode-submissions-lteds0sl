class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = Counter(nums)

        for i in range(3):
            for j in range(count[i]):
                nums[index] = i
                index += 1
