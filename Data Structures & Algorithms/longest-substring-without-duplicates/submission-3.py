class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        longest = 0

        if len(set(s)) == 1:
            return 1
        
        while r < len(s):
            set_l = len(set(s[l:r+1]))
            list_l = len(s[l:r+1])

            if set_l == list_l:
                longest = max(set_l,longest)
                r = r + 1
            else:
                l = l + 1
        
        return longest