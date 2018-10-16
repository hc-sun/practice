class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': #island_num+1 when encounter new island 
                    self.dfs(grid, i, j)
                    island_num += 1
        return island_num
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': # check meet edges or if it's 0
            return
        grid[i][j] = '0' # mark as visited
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3