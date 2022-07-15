class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = list(jewels)
        counter = collections.Counter(list(stones))
        
        result = 0
        for x in jewel:
            result += counter[x]
        
        return result