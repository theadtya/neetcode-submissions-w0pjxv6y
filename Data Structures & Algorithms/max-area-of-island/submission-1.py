class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (
                r <0 or
                r > rows-1 or
                c < 0 or
                c > cols-1 or
                (r,c) in visited or 
                grid[r][c]==0
            ):
                return 0
            
            visited.add((r,c))
            area=1
            area+= dfs(r,c-1)
            area+= dfs(r,c+1)
            area+= dfs(r-1,c)
            area+= dfs(r+1,c)

            return area
            
        visited=set()
        rows= len(grid)
        cols= len(grid[0])
        maxarea= 0
        for r in range(rows):
            for c in range(cols):
                maxarea= max(maxarea,dfs(r,c))
        return maxarea