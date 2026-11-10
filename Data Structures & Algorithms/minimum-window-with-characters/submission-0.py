from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        count = 0
        l = 0
        k = -1
        mi = float("inf")

        for r, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] <= need[char]:
                count += 1

            while count == len(t):
                current_window_size = r - l + 1
                if current_window_size < mi:
                    mi = current_window_size
                    k = l
                
                left_char = s[l]

                if left_char in need and window[left_char] == need[left_char]:
                    count -= 1
                window[left_char] -= 1

                l += 1

        return "" if k == -1 else s[k: k + mi]
