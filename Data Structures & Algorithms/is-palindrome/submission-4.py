class Solution:
    def isPalindrome(self, s: str) -> bool:
        real_s = ""
        for ch in s:
            if ch.isalnum():
                real_s += ch.lower()
        print(real_s[::-1] , real_s)
        return real_s[::-1] == real_s