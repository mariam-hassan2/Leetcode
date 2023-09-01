class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)
        
        for i in s:
            m[i] += 1

        #need to create a dictionary and add each character with how many times it appears in the string  
        #so you would incremenet it's key whenever it's encountered
        k = defaultdict(int)
        for j in t:
            k[j]+=1

        return m==k
        
