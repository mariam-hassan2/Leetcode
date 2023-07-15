class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        numRows = len(grid)
        numColumns = len(grid[0])
        visit = set()
        numislands = 0


        def bfs(row, column):

            queue = collections.deque()
            visit.add((row,column))
            queue.append((row,column))


            while queue:
                k,m = queue.popleft()
                directs = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directs:
                    r,c = k + dr, m + dc
                    if (r in range(numRows) and c in range (numColumns) and grid[r][c] == "1" and (r,c) not in visit):
                        queue.append((r,c))
                        visit.add((r,c))
                        

        for i in range(numRows):
            for j in range(numColumns):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    numislands += 1    

                    
        return numislands
