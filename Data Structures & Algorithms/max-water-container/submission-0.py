class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        for i in range(len(heights)):
            for j in range(0,len(heights)):
                if i == j:
                    continue
                length = abs(i-j)
                height = min(heights[i],heights[j])
                area = length * height
                max_amt = max(max_amt,area)

        return max_amt
