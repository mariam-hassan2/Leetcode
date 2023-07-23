class Solution:

    def solve(self, board: list[list[str]]) -> None:
        if len(board)== 1: return;
        """
        Do not return anything, modify board in-place instead.
        """
        
        numRows = len(board)
        numColumns = len(board[0])
        
        def bfs(row,column):
            visit = set()
            flag = False
            q = collections.deque()
            q.append((row,column))
            visit.add((row,column))
            if row == 0 and board[row][column] == "O" or column == 0 and board[row][column] == "O" : flag = True
            if row == numRows - 1 and board[row][column] == "O" or column == numColumns - 1  and board[row][column] == "O" : flag = True            
            while q:
                k,m = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c = k + dr, m + dc
                    if r == 0 and c in range(numColumns) and board[r][c] == "O" or c == 0 and r in range(numRows) and board[r][c] == "O" : 
                        flag = True
                    if r == numRows-1 and c in range(numColumns) and board[r][c] == "O" or c == numColumns -1 and r in range(numRows) and board[r][c] == "O" : 
                        flag = True                       
                    if r in range(numRows) and c in range(numColumns) and board[r][c] == "O" and (r,c) not in visit: 
                        q.append((r,c))
                        visit.add((r,c))
                
            if flag == False:
                for s,t in visit:
                    board[s][t] = "X"

                    
                
        for i in range(numRows):
            for j in range(numColumns):
                if(board[i][j] == "O"):
                    bfs(i,j)