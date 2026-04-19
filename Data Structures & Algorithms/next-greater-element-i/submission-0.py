class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hm = {}

        for n in nums2:
            while stack and stack[-1] < n:
                hm[stack.pop()] = n
            stack.append(n)

        while stack:
            hm[stack.pop()] = -1
        
        return [hm[n] for n in nums1]