class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, a, n):
        #Code here
        tnm=-1
        h=len(a)-1
        x=[]
        while(h>=0):
            if a[h]>=tnm:
                x.append(a[h])
                tnm=a[h]
            h-=1
        k=x[::-1]
        return k

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends