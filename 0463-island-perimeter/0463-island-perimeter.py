class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        if not grid: return 0
        if len(grid) == 1 and len(grid[0]) == 1: return 4


        numRows = len(grid)
        numColumns = len(grid[0])
        visit = set()

        
        def bfs(row, column):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q = collections.deque()
            visit.add((row,column))
            q.append((row,column))

            while q:
                k,m = q.popleft()
                for dr,dc in directions:
                    r = dr + k
                    c = dc + m
                    if(r in range(numRows) and c in range(numColumns) and
                     grid[r][c]== 1 and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        ans = 0
            
        def neigbors(x,y)-> int:
            perimeter = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                r = dr + x
                c = dc + y
                
                if(r in range(numRows) and c in range(numColumns) and
                grid[r][c]== 0):  
                    perimeter += 1
                elif r not in range(numRows) or c not in range(numColumns):
                    perimeter += 1

            return perimeter

            
        for i in range(numRows):
            for j in range(numColumns):
                if grid[i][j] == 1 and (i,j) not in visit:
                    bfs(i,j)                
                    
        for a,b in visit:
            m = neigbors(a,b)
            ans += m
            

        return ans


