# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([[root,0]])
        mx=0
        while(len(q)):
            k1=q[-1][1]-q[0][1]+1
            mx=max(mx,k1)
            n=len(q)
            for i in range(n):
                k=q.popleft()
                if k[1]!=0:
                    k[1]-=1
                if k[0].left:
                    q.append([k[0].left,2*k[1]+1])
                if k[0].right:
                    q.append([k[0].right,2*k[1]+2])
        return mx
        
                





