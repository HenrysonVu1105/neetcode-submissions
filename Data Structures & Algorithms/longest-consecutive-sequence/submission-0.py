class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        streak = 0

        for num in set_nums:
            if (num -1) not in set_nums:
                current = num
                cur_streak = 1
                while ( current + 1) in set_nums:
                    current += 1
                    cur_streak +=1

                streak = max(streak, cur_streak)

        return streak
                    