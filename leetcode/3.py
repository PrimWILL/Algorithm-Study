class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        s = '0' + s
        result = 0
        
        char_check = collections.defaultdict(int)
        temp = 1
        for i in range(1, len(s)):
            if char_check[s[i]] > 0:
                result = max(result, i - temp)
                temp = max(temp, char_check[s[i]] + 1)
            char_check[s[i]] = i
        
        result = max(result, len(s) - temp)
        
        return result