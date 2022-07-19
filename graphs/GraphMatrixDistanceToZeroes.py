from collections import deque

class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()
        visited = set()
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
            
        while q:
            r, c, d = q.popleft()
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    grid[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))
                    visited.add((nr, nc))
        return grid