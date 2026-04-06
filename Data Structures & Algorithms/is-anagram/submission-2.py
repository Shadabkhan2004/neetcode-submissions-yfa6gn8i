class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp1 = {}
        mp2 = {}

        for ch in s:
            if ch not in mp1.keys():
                mp1[ch] = 1
            else:
                mp1[ch] += 1
        
        for ch in t:
            if ch not in mp2.keys():
                mp2[ch] = 1
            else:
                mp2[ch] += 1

        # print(mp1)
        # print(mp2)
        for key in mp1.keys():
            if mp1.get(key,0) != mp2.get(key,0):
                return False

        return True
