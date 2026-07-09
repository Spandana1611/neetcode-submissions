class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = [[sorted(i),i] for i in strs]
        s.sort()
        ans = [[s[0][1]]]
        for i in range(1, len(strs)):
            if s[i][0] == s[i-1][0]:
                ans[-1].append(s[i][1])
            else:
                ans.append([s[i][1]])
        return ans