# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
# from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hs={}     
        q=[[root,0]]
        while(len(q)):
            n=len(q)
            a1={}
            for i in range(n):
                k=q.pop(0)
                knode,kpos=k[0],k[1]
                if kpos not in a1:
                    a1[kpos]=[k[0].val]
                else:
                    a1[kpos].append(k[0].val)
                
                if knode.left:
                    q.append([knode.left,kpos-1])
                if knode.right:
                    q.append([knode.right,kpos+1])
            for i in a1:
                if len(a1[i])>1:
                    a1[i].sort()
                if i not in hs:
                    hs[i]=[i1 for i1 in a1[i]]
                else:
                    for j in a1[i]:
                        hs[i].append(j)
                
            
        d1=sorted(hs)
        x=[]
        print(hs)
        for i in d1:
            x.append(hs[i])
        return x

