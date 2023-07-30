class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        id = [i for i in range(n)]
        size = [1]*n
        
        def find(c):
            res = c
            while res != id[res]:
                id[res] = id[id[res]]
                res = id[res]
            return res
            
        def union(c1,c2):
            
            r1,r2 = find(c1),find(c2)
            
            if r1 == r2:
                return 0
            if size[r1]>size[r2]:
                id[r1] = r2
                size[r1]+=size[r2]
            else:
                id[r2] = r1
                size[r2]+=size[r1]
            
            return 1
        
        ans = n
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    ans -= union(i,j)
                
                
            
        return ans      
        