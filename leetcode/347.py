class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        result = [val for val, count in counter.most_common(k)]

        return result
