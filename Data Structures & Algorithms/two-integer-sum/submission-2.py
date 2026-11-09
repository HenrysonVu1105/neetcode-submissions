class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        n = len(nums)

        for i in range(n):
            x = target - nums[i]
            if x in hashmap:
                return [hashmap[x],i]
            
            hashmap[nums[i]] = i

        return []