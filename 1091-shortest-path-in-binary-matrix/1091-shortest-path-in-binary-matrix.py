class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        dist=[]
        n=len(g)
        if n==1:
            if g[0][0]==0:
                return 1
        for i in range(n):
            dist.append([int(100000) for j in range(n)])
        if g[0][0] or g[-1][-1]:
            return -1
        dist[0][0]=0
        q=[[1,0,0]]
        d1=[1,-1,1,-1,1,0,-1,0]
        d2=[1,-1,-1,1,0,1,0,-1]
        while(len(q)):
            d,i,j=q.pop(0)
            for k in range(8):
                x=i+d1[k]
                y=j+d2[k]
                if x>=0 and x<n and y>=0 and y<n and g[x][y]!=1:
                    if dist[x][y]>1+d:
                        dist[x][y]=1+d
                        q.append([1+d,x,y])
                        if x==n-1 and y==n-1:
                            return 1+d
        return -1
            


        