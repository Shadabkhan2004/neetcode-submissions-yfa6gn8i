class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for ch in s:
            if ch == '{' or ch=='[' or ch=='(':
                stack.append(ch)
            elif ch == '}' or ch==']' or ch==')':
                if len(stack) == 0:
                    return False
                corr_ele = mp[ch]
                top_ele = stack.pop()
                # print(corr_ele,top_ele)
                if corr_ele != top_ele:
                    return False

        return len(stack) == 0
