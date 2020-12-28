class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        adjacent = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                if (i > 0) and (grid[i][j] == 1):
                    if grid[i - 1][j] == 1:
                        adjacent += 1
                if (j > 0) and (grid[i][j] == 1):
                    if grid[i][j - 1] == 1:
                        adjacent += 1
            perimeter -= (2 * adjacent)
            adjacent = 0
        
        return perimeter
