import random

# 3.59 ms ± 65.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
def numIslands(grid):
    if not grid:
        return 0        
    
                    
    def sinkIsland(r, c):
        if grid[r][c] == '1':
            grid[r][c] = '0'
            if r > 0:
                sinkIsland(r-1, c)
            if r < R:
                sinkIsland(r+1, c)
            if c > 0:
                sinkIsland(r, c-1)
            if c < C:
                sinkIsland(r, c+1)


    R = len(grid) - 1
    C = len(grid[0]) - 1
    numIslands = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                sinkIsland(r, c)
                numIslands += 1

    return numIslands

# 20.3 ms ± 93.4 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
def numIslandsMap(grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


def generateRandomGrid():
    m = n = 300
    return [[str(random.randint(0, 1)) for _ in range(m)] for _ in range(n)]

# 3.52 ms ± 21.8 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
def numIslandsVisited(grid):
    m, n = len(grid), len(grid[0])
    count, visited = 0, set()

    # drown the connected landmass 
    def dfs(r, c, grid, visited):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1' or (r,c) in visited:
            return
        
        visited.add((r,c))
        
        dfs(r + 1, c, grid, visited)
        dfs(r - 1, c, grid, visited)
        dfs(r, c + 1, grid, visited)
        dfs(r, c - 1, grid, visited)

    # iterate over matrix to find an island        
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i,j) not in visited:
                count += 1
                dfs(i, j, grid, visited)                                     

    return count