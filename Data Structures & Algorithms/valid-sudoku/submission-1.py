class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                r_key = f'row {r}:{val}'
                c_key = f'col {c}:{val}'
                b_key = f'box {r//3}, {c//3}: {val}'

                if r_key in seen or c_key in seen or b_key in seen:
                    return False

                seen.add(r_key)
                seen.add(c_key)
                seen.add(b_key)

        return True