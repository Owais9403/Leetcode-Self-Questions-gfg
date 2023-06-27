#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,a):
        #code here
        d1=[1,0,-1,0,-1,1,-1,1]
        d2=[0,1,0,-1,1,-1,-1,1]
        def dfs(i,j):
            if vis[i][j]==1:
                return 
            vis[i][j]=1
            for k in range(8):
                x=i+d1[k]
                y=j+d2[k]
                if x>=0 and x<n and y>=0 and y<m and a[x][y]==1 and vis[x][y]==0:
                    dfs(x,y)


        c=0
        n=len(a)
        m=len(a[0])
        vis=[]
        for i in range(n):
            vis.append([0 for j in range(m)])
        for i in range(n):
            for j in range(m):
                if a[i][j]== 1 and vis[i][j]==0:
                    c+=1
                    dfs(i,j)
        return c 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends