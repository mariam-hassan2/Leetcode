class Solution:
        def findOrder(self, numCourses:int, prerequisities:list[list[int]])->list[int]:
        
            prereq = {c:[] for c in range(numCourses)}
            
            for crs,pre in prerequisities:
                prereq[crs].append(pre)
            
            T = []
            visit,cycle = set(),set()
            def dfs(crs):
                if crs in cycle:
                    return False
                if crs in visit:
                    return True
                cycle.add(crs)
                for pre in prereq[crs]:
                    if dfs(pre) == False: return False
                
                cycle.remove(crs)
                visit.add(crs)
                T.append(crs)
                return True
        
            for c in range(numCourses):
                if dfs(c) == False:
                    return []
                
            return T    
