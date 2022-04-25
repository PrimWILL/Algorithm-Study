class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[nums[i], i] for i in range(len(nums))]
        new_nums.sort(key=lambda x : x[0])
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if new_nums[left][0] + new_nums[right][0] == target:
                return [new_nums[left][1], new_nums[right][1]]
            elif new_nums[left][0] + new_nums[right][0] > target:
                right -= 1
            else:
                left += 1
            