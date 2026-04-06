class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for num in nums:
            if num not in mp.keys():
                mp[num] = 1
            else:
                mp[num] += 1
        

        for value in mp.values():
            if value > 1:
                return True

        return False
        