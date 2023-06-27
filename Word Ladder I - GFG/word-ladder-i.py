from collections import deque
class Solution:
	def wordLadderLength(self, s, f, w):
		#Code here
		q=deque([[s,1]])
        w=set(w)
        n=len(s)
        # print(w)
        if f not in w:
            return 0
        while(len(q)):
            a,k=q.popleft()
            if a==f:
                return k
            if a in w:
                w.remove(a)
            for i in range(n):
                for j in range(26):
                    if i!=n-1:
                        if a[:i]+chr(97+j)+a[i+1:] in w:
                            q.append([a[:i]+chr(97+j)+a[i+1:],k+1])
                    else:
                        if a[:i]+chr(97+j) in w:
                            q.append([a[:i]+chr(97+j),k+1])
                    
        return 0


#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends