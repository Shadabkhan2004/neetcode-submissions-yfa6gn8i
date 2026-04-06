class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            if nums[i] not in mp.keys():
                mp[nums[i]] = i
            
            rem = target - nums[i]
            if rem in mp.keys():
                j = mp[rem]
                if i!= j:
                    if i > j:
                        return [j,i]
                    else:
                        return [i,j]
        