class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        k=0
        x=''
        for i in range(len(s)):
            if k==0:
                k=1
                continue
            if s[i]=='(':
                k+=1
                if k:
                    x+='('
            else:
                k-=1
                if k:
                    x+=')'
        return x
            


            
