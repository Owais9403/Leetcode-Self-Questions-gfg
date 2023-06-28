#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, n, a):
        # code here
        q=[]
        ind=[0]*n
        res=[]
        vis=[0]*n
        for i in range(n):
            for j in a[i]:
                ind[j]+=1
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        while(len(q)):
            k=q.pop(0)
            res.append(k)
            vis[k]=1
            for i in a[k]:
                ind[i]-=1
                if ind[i]==0 and vis[i]==0:
                    q.append(i)
        # print(res)
        return len(res)!=n
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends