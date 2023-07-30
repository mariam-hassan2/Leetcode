class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        id = [i for i in range(n+1)]
        size = [1] * (n+1)
        
        def find(c):
            res = id[c]
            while res != id[res]:
                id[res] = id[id[res]]
                res = id[res]
            return res
        
        def union(c1,c2):
            r1,r2 = find(c1),find(c2)
            
            if r1 == r2:
                return False
            
            if size[r1] > size[r2]:
                id[r1] = r2
                size[r1] += size[r2]
            else:
                id[r2] = r1
                size[r2] += size[r1]
                return True
                
        
        for i,j in edges:
            if not union(i,j):
                return [i,j]

