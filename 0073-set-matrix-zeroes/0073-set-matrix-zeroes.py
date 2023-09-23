class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroidx = deque()
        numRows = len(matrix)
        numColumns = len(matrix[0])
        for i in range(numRows):
            for j in range(numColumns):
                if matrix[i][j]== 0:
                    zeroidx.append((i,j))
        
        while zeroidx:
            r,c = zeroidx.popleft()
            for m in range(numColumns):
                matrix[r][m] = 0
            for n in range(numRows):
                matrix[n][c] = 0

        