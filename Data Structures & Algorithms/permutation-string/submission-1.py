class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = [0 for _ in range(26)]
        for i in s1:
            l[ord(i)-ord('a')] += 1

        for i in range(0, len(s2)-len(s1)+1):
            if l[ord(s2[i]) - ord('a')] > 0:
                c = 1
                x = i+1
                l1 = l.copy()
                l1[ord(s2[i]) - ord('a')] -= 1
                while x<len(s2) and c<len(s1) and l1[ord(s2[x]) - ord('a')] > 0:
                    l1[ord(s2[x]) - ord('a')] -= 1
                    c+=1
                    x+=1
                if c == len(s1):
                    return True
        return False
