class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:  #prereq [0 (course), 1 (prereq)]
            premap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited: return False
            if premap[crs] == []: return True
            
            visited.add(crs)
            
            for pre in premap[crs]:
                if not dfs(pre): return False
            
            visited.remove(crs)
            premap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True