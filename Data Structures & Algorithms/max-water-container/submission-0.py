class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r=0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                r = max(r, min(heights[i], heights[j]) * (j-i))

        return r
        