from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []

        for item, count in counts.most_common(k):
            res.append(item)

        return res
