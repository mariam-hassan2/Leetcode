class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = word.upper()
        lower = word.lower()
        if word == upper or word == lower:
            print(upper)
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else: return False
        