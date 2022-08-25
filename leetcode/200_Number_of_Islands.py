class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += self.dfs(visited, grid, i, j, 0)
        
        return result
        
    def dfs(self, visited: List[List[str]], grid: List[List[str]], x:int, y:int, cnt: int) -> int:
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return cnt
        
        if visited[x][y] == 1:
            return cnt
        
        visited[x][y] = 1
        if grid[x][y] == "1":
            cnt = 1
            self.dfs(visited, grid, x - 1, y, cnt)
            self.dfs(visited, grid, x + 1, y, cnt)
            self.dfs(visited, grid, x, y - 1, cnt)
            self.dfs(visited, grid, x, y + 1, cnt)
        
        return cnt
