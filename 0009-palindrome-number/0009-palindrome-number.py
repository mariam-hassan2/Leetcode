class Solution:
    def isPalindrome(self, x: int) -> bool:
        def get_pos(num):
            pos_nums = []
            while num != 0:
                pos_nums.append(num%10)
                num = num // 10
            return pos_nums

        if(x < 0): return False
        res = get_pos(x)
        left = 0
        right = len(res) -1

        while left <= right:
            if res[left] == res[right]:
                left +=1
                right -=1
            else: return False
        return True



