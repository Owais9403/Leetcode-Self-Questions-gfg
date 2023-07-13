#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,a, n, k): 
       #Write your code here
    #   print(k)
       i=0
       s=0
       if k==0:
           return [-1]
       for j in range(n):
           s+=a[j]
           if s>k:
               while(i<n and s>k):
                   s-=a[i]
                #   print(s)
                   i+=1
        #   print(s)
           if s==k:
               return [i+1,j+1]
       return [-1]
               
           
           
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends