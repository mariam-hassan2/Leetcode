class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1: return mat[0][0]
        s = 0
        n = len(mat) 
     
        for i in range(n):
            s += mat[i][i]

        for i in range(n):
            s += mat[i][n-i-1]

        if len(mat) % 2 == 0: return s
        l = (len(mat)//2)
        return s - mat[l][l]