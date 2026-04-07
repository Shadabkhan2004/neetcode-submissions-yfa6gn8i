class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        freq = {}
        bucket = []

        for _ in range(len(nums) + 2):
            bucket.append([])
        
        for i,n in enumerate(nums):
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        
        for key,value in freq.items():
            bucket[value].append(key)
    
        result = []

        for i in range(len(bucket)-1,-1,-1):
            if len(result) == k:
                break
            for ele in bucket[i]:
                result.append(ele)
        
        return result

