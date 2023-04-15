#User function Template for python3


class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        hs={}     
        q=[[root,0]]
        while(len(q)):
            n=len(q)
            a1={}
            for i in range(n):
                k=q.pop(0)
                knode,kpos=k[0],k[1]
                if kpos not in a1:
                    a1[kpos]=[k[0].data]
                else:
                    a1[kpos].append(k[0].data)
                
                if knode.left:
                    q.append([knode.left,kpos-1])
                if knode.right:
                    q.append([knode.right,kpos+1])
            for i in a1:
                if i not in hs:
                    hs[i]=[i1 for i1 in a1[i]]
                else:
                    for j in a1[i]:
                        hs[i].append(j)
                
            
        d1=sorted(hs)
        x=[]
        # print(hs)
        # print(d1)
        for i in d1:
            for j in hs[i]:
                x.append(j)
        return x



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input()) 
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()



# } Driver Code Ends