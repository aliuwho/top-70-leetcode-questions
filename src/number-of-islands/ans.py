class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1'):
                    count += 1
                    self.transformIsland(grid, i, j)
        return count

    def transformIsland(self, grid, i, j):
        if grid[i][j] == '1':
            grid[i][j] = '2'
            if i > 0:
                self.transformIsland(grid, i - 1, j)
            if j > 0:
                self.transformIsland(grid, i, j - 1)
            if i + 1 < len(grid):
                self.transformIsland(grid, i + 1, j)
            if j + 1 < len(grid[0]):
                self.transformIsland(grid, i, j + 1)
