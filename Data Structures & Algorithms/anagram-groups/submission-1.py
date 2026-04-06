from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            sorted_s = str(list(sorted(s)))
            mp[sorted_s].append(s)
            
        result = list(mp.values())
        
        return result