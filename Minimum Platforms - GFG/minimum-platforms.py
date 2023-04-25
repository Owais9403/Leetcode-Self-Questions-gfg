#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,a,d):
        # code here
        a.sort()
        d.sort()
        i,j=1,0
        p=1
        
        m=1

        while(i<n):
            if a[i]<=d[j]:
                i+=1
                p+=1
                m=max(m,p)
            else:
                j+=1
                p-=1
        return m
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends