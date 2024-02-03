class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        row_len=len(grid)
        col_len=len(grid[0])
        def look_around(row,col):
            peri=4
            expected=((1,0),(-1,0),(0,1),(0,-1))
            for i in expected:
                if 0<=row+i[0]<row_len and 0<=col+i[1]<col_len:
                    if grid[row+i[0]][col+i[1]]==1:
                        peri-=1
            return peri
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res+=look_around(i,j)
        return res