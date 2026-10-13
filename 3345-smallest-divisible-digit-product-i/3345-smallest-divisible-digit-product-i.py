class Solution:
    def smallestNumber(self, n: int, t: int) -> int: 
        p=1
        while p%t!=0:
            i=n
            p=1
            while i>0:
                q=i%10
                p*=q
                i=i//10 
            if p%t==0:
                return n 
            n+=1
        return n


            
        