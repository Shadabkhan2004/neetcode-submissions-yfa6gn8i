class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        freq = []

        for i in range(len(nums)+1):
            freq.append([])

        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] += 1
        
        for key,value in mp.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1,-1,-1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) == k:
                    return res