class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        mp = {}

        for _ in range(len(nums)+1):
            bucket.append([])

        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for n,i in mp.items():
            bucket[i].append(n)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if len(res) == k:
                break
            for ele in bucket[i]:
                res.append(ele)
                if len(res) == k:
                    break

        return res
