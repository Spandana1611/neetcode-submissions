class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = [0 for _ in range(52)]
        for i in t:
            if i.islower(): l[ord(i)-ord('a')] += 1
            else: l[26+ord(i)-ord('A')] += 1
        ans = None
        for i in range(len(s)-len(t)+1):
            if (s[i].islower() and l[ord(s[i])-ord('a')] > 0) or (s[i].isupper() and l[ord(s[i])-ord('A')+26] > 0):
                x = i+1
                c = 1
                a = s[i]
                l1 = l.copy()
                if s[i].islower(): l1[ord(s[i])-ord('a')] -= 1
                else: l1[26 + ord(s[i])-ord('A')] -= 1
                while c<len(t) and x<len(s):
                    if s[x].islower() and l1[ord(s[x])-ord('a')] > 0:
                        l1[ord(s[x])-ord('a')] -= 1
                        c+=1
                    elif s[x].isupper() and l1[26+ord(s[x])-ord('A')] > 0:
                        l1[26+ord(s[x])-ord('A')] -= 1
                        c+=1
                    a += s[x]
                    x+=1
                if c==len(t):
                    if ans is None:
                        ans = a
                    elif len(ans) > len(a):
                        ans = a
        if ans is None:
            return ""
        return ans
