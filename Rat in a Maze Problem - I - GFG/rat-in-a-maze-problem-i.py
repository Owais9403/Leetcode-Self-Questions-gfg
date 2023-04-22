#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        dl=[1,0,0,-1]
        dr=[0,-1,1,0]
        ans=[]
        s=[]
        id=0
        jr=0
        st='DLRU'
        def ss(ans,m,n,s,dl,dr,id,jr,vs):
            if m[id][jr]==0:
                return 
            if id==n-1 and jr==n-1:
                k1=''.join(s)
                ans.append(k1)
            for i in range(4):
                l=id+dl[i]
                h=jr+dr[i]
                if l<n and l>=0 and h<n and h>=0 and m[l][h]==1 and vs[l][h]==0:
                    s.append(st[i])
                    vs[id][jr]=1
                    ss(ans,m,n,s,dl,dr,l,h,vs)
                    vs[id][jr]=0
                    s.pop()
        vs=[[0 for i in range(n)] for i in range(n)]
        ss(ans,m,n,s,dl,dr,id,jr,vs)
        return ans
                    
                    
                    
                    
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends