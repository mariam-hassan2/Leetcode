class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = max(len(word1),len(word2))
        ans = ""
        for i in range(n):
            if i in range(len(word1)) and i in range(len(word2)):
                ans+= word1[i]
                ans+= word2[i]
            elif i in range(len(word1)):
                ans += word1[i:n]
                return ans
            else:
                ans += word2[i:n]
                return ans 

        return ans 

        