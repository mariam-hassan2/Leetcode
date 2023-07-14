class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not List: return null
        numRows = len(image)
        numColumns = len(image[0])
        col = image[sr][sc]
        visit = set()
        def bfs(sr,sc):
            q = collections.deque()
            q.append((sr,sc))
            visit.add((sr,sc))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                k,m = q.popleft()
                for dr,dc in directions:
                    r = k + dr
                    c = m + dc
                    if (r in range(numRows) and c in range(numColumns) and 
                    image[r][c] == col and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        bfs(sr,sc)


        for x,y in visit:
            image[x][y] = color


        return image
                




