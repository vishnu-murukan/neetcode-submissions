class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=[1] * (len(nums))
        prefix=1
        for i in range(len(nums)):
            mul[i] = prefix
            prefix *= nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            mul[i] *= post
            post *= nums[i]

        return mul


        