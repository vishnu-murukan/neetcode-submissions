class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r=0
        s= set(nums)
         
        for num in nums:
            streak = 0
            curr = num
            while curr in s:
                streak += 1
                curr += 1
            r = max(r,streak)
        return r