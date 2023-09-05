class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        
        def get_pos(num):
            pos_num = []
            while num != 0:
                pos_num.append(num%10)
                num = num // 10
            return pos_num

        res = get_pos(left)
        ans = []
        for i in range(left,right+1):
            res = get_pos(i)
            counter = 0
            for j in res:  
                if j != 0 and i % j  == 0:
                    counter +=1
            if counter == len(res): ans.append(i)
        return ans
        






 