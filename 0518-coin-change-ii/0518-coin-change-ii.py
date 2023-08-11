class Solution:
    def change(self, t: int, a: List[int]) -> int:
        def f(i,t):
            if i<0:
                return 1 if t==0 else 0
            if dp[i][t]!=-1:
                return dp[i][t]
            nottake=f(i-1,t)
            take = 0
            if t>=a[i]:
                take=f(i,t-a[i])
            dp[i][t]=take+nottake
            return take+nottake

        dp=[]
        n=len(a)
        for i in range(n):
            dp.append([-1 for j in range(t+1)])
        return f(n-1,t)
        
