# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        a=fromm
        b=aux
        c=to
        n=N
        def tohh(n,a,b,c):
            if n==1:
                print("move disk",n,"from rod",a,"to rod",c)
                return 
            tohh(n-1,a,c,b)
            print("move disk",n,"from rod",a,"to rod",c)
            tohh(n-1,b,a,c)
        tohh(n,a,b,c)
        k=(2**n) - 1
        return k
        
        
        # Your code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends