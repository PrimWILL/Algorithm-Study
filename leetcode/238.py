class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = list()
        for x in range(len(nums)):
            result.append(p)
            p = p * nums[x]
        
        p = 1
        for x in reversed(range(len(nums))):
            result[x] *= p
            p = p * nums[x]
        
        return result