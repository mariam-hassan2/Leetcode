class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ": return True
        if len(s) == 1: return True


        c = ""
        for i in s:
            if i.isalnum():
                c+=i.lower()
        if not c: 
            return True
        left = 0
        right = len(c) -1

        while left <= right:
            if c[left].lower() == c[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True

    