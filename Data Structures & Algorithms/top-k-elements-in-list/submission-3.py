from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])

        for num, freq in counts.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         res = []

#         for item, count in counts.most_common(k):
#             res.append(item)

#         return res
