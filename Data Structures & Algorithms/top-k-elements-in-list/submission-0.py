class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for n in nums:
            if n not in mp.keys():
                mp[n] = 1
            else:
                mp[n] += 1
        
        mp = dict(sorted(mp.items(),key= lambda x : x[1],reverse=True))

        count = 0
        res = []

        for key in mp.keys():
            if count == k:
                break
            res.append(key)
            count += 1

        return res
        
