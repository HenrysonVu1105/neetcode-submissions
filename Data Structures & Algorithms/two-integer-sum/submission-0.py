class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)

        for i in range(n):
            
            x = target - nums[i]
            if x in h:
                return [h[x], i]
            h[nums[i]] = i
        
        return[]
            