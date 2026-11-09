class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        count = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_idx = stack.pop()

                count[prev_idx] = i - prev_idx

            stack.append(i)
        
        return count



