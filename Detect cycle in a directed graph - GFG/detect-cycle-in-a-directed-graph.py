#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, n, x):
        # code here
        def dfs(x):
            vis[x]=1
            pvis[x]=1
            for i in a[x]:
                
                if vis[i]==0:
                    if dfs(i)==1:
                        return 1        
                elif pvis[i]==1:
                    return 1
            pvis[x]=0
            return 0

        a={}
        for i in range(n):
            a[i]=x[i]
        vis=[0]*(n)
        pvis=[0]*(n)
        
        for i in range(n):
            if vis[i]!=1:
                if dfs(i)==1:
                    return 1
        return 0
        
        


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