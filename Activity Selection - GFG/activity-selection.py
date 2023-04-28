#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,s,e):
        a=[]
        for i in range(n):
            a.append([e[i],s[i]])
        a.sort()
        k=[a[0]]
        d=a[0]
        for i in range(1,n):
            if d[0]<a[i][1]:
                k.append(a[i])
                d=a[i]
        return len(k)
            
        

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends