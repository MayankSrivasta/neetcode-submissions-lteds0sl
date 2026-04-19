class Solution:
    def subarraySum(self, nums, k):

        hm = {0:1}
        prefix_sum = 0
        count = 0

        for num in nums:

            prefix_sum += num
            diff = prefix_sum - k

            if diff in hm:
                count += hm[diff]

            hm[prefix_sum] = hm.get(prefix_sum,0) + 1

        return count