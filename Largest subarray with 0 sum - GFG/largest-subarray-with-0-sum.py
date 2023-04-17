#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        a=[]
        c=0
        for i in arr:
            c+=i
            a.append(c)
        s={}
        #print(a)
        k=0
        k1=0
        for i in range(n):
            s[a[i]]=i
        #print(s)
        for i in range(n):
            if(a[i]==0):
                k1=i+1
        for i in range(n):
            #print(a[i])
            if(a[i] in s):
                #print(s[a[i]])
                x=abs(s[a[i]]-i)
                k=max(x,k)
                #print(k)
        if(a[-1]==0):
            return n
        else:
            
            return max(k,k1)
            
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends