#User function Template for python3

class Solution:
    def firstNonRepeating(self, a, n): 
        # Complete the function
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in a:
            if d[i]==1:
                return i
        return 0
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends