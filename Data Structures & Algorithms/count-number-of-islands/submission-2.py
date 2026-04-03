class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if (
                r <0 or 
                r> rows-1 or 
                c<0 or 
                c > cols-1 or 
                grid[r][c]=="0" or 
                (r,c) in seen
            ):
                return False
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

            return True
        
        seen= set()
        rows,cols= len(grid),len(grid[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c):
                    count+=1
        return count

        

