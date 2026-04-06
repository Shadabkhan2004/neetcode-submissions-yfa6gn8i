class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for i in range(len(strs)):
            length = len(strs[i])
            encoded_string += (str(length) + "#" + strs[i])
            
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []

        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_strings.append(s[j+1:j+length+1])
            i = j + length + 1
        
        return decoded_strings
        