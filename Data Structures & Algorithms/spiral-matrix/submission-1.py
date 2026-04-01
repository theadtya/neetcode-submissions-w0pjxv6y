class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        def dfs(rows, cols, r, c, dr, dc):
            if rows == 0 or cols == 0:
                return

            for i in range(cols):
                r += dr
                c += dc
                res.append(matrix[r][c])

            dfs(cols, rows - 1, r, c, dc, -dr)

        dfs(rows, cols, 0, -1, 0, 1)
        return res