class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = []
        for i in range(len(temperatures)):
            if i>0:
                j = i-1
                while j>=0:
                    if temperatures[i] > temperatures[j] and s[j] == 'f':
                        ans[j]+=1
                        s[j] = 't'
                    elif s[j] == 'f':
                        ans[j]+=1
                    j-=1
            
            s.append('f')
            ans.append(0)
        for i in range(len(s)):
            if s[i] == 'f':
                ans[i] = 0
        return ans
