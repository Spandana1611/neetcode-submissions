class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d = defaultdict(int)
        ans = 1
        max_l = 1
        i = 1
        d[s[0]] = 1
        while i<len(s):
            if d[s[i]] > 0:
                ans = max(max_l, ans)
                i = d[s[i]] + 1
                d = defaultdict(int)
                d[s[i-1]] = i
                max_l = 1
            else:
                d[s[i]] = i+1
                max_l+=1
                i+=1
        return max(ans, max_l)

