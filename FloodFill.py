import random

def floodFill(image, sr, sc, newColor):
    startColor = image[sr][sc]
    if startColor == newColor:
        return image

    R = len(image) - 1
    C = len(image[0]) - 1

    def floodFillRecurs(r, c):
        if image[r][c] == startColor:
            image[r][c] = newColor
            if r > 0:
                floodFillRecurs(r-1, c)
            if r < R:
                floodFillRecurs(r+1, c)
            if c > 0:
                floodFillRecurs(r, c-1)
            if c < C:
                floodFillRecurs(r, c+1)

    floodFillRecurs(sr, sc)

    return image


def floodFillSol(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r-1, c)
            if r+1 < R: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c+1 < C: dfs(r, c+1)

    dfs(sr, sc)
    return image


def createRandom2dList():
    n = random.randint(1, 50)
    m = random.randint(1, 50)
    return [[random.randint(0, 3) for _ in range(n)] for _ in range(m)]