class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        
        # 돌(S)의 빈도 수 계산
        for char in stones:
            freqs[char] += 1
        
        # 보석(J)의 빈도 수 합산
        for char in jewels:
            count += freqs[char]
        
        return count