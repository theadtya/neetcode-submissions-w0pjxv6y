class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen=set()
        maxarea= 0

        def dfs(r,c):
            if (
                r <0 or
                r > len(grid)-1 or
                c < 0 or
                c > len(grid[0])-1 or
                (r,c) in seen or 
                grid[r][c]==0
            ):
                return 0
            
            seen.add((r,c))
            area=1
            area+= dfs(r,c-1)
            area+= dfs(r,c+1)
            area+= dfs(r-1,c)
            area+= dfs(r+1,c)

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxarea= max(maxarea,dfs(r,c))
        return maxarea