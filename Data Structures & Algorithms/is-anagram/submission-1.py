class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = [i for i in s]
        lt = [i for i in t]
        ls.sort()
        lt.sort()
        return ls == lt
