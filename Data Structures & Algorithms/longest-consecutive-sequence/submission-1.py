class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mp = set(nums)

        for i,n in enumerate(nums):
            if n-1 not in mp:
                long = 0
                while n + long in mp:
                    long += 1
                longest = max(longest,long)
        return longest