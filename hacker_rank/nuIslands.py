from typing import * 

class Solution:
    def isNewLandNeighbour(self, t:tuple, rows, cols, grid,notVisited):
        (m,n) = t
        if min(m,n) < 0 : 
            return False
        if m >= rows : return False
        if n >= cols : return False 
        if grid[m][n] == '0' : return False
        if (m,n) not in notVisited : return False 
        return True

    def neighbours(self, gridPoint:tuple, grid, rows, cols,notVisited)->Set[tuple]:
        (i,j) = gridPoint
        upDown = [(m,j) for m in [i-1,i+1] if self.isNewLandNeighbour((m,j),rows,cols,grid,notVisited) ]
        lftRgt = [(i,n) for n in [j-1,j+1] if self.isNewLandNeighbour((i,n),rows,cols,grid,notVisited) ]
        return set(set(upDown).union(lftRgt))

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # make the set of land points that we must visit 
        notVisited = set([(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"])
        islandCount = 0 
        while notVisited:
            startPoint = notVisited.pop()
            islandCount += 1
            nSet = self.neighbours(startPoint, grid, rows, cols,notVisited)
            while nSet:
                p = nSet.pop()
                if p not in notVisited: 
                    continue
                notVisited.remove(p)
                nSet = nSet.union(self.neighbours(p, grid, rows, cols,notVisited))

        return islandCount 

    

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

print(Solution().numIslands(grid))