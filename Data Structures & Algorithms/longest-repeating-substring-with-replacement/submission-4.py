class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1
        ans = 1
        r = 0
        ch = None
        r_idx = None
        while j<len(s):
            if s[j] != s[i]:
                if r+1 <= k: 
                    if r_idx is None:
                        r_idx = j
                    r+=1
                    j+=1
                else:
                    # print(i, j, r, r_idx)
                    ans = max(min(j-i+k-r,len(s)), ans)
                    if r_idx is None:
                        i+=1
                    else:
                        i = r_idx
                        r_idx = None
                    j = i+1
                    r=0
                    r_idx = None
            else:
                j+=1
            if j >= len(s):
                # print(i, j, r, r_idx, "2")
                ans = max(min(j-i+k-r,len(s)), ans)
                if r_idx is None:
                    i+=1
                else:
                    i = r_idx
                    r_idx = None
                j = i+1
                r=0
                r_idx = None
        # print(i, j, r, r_idx, "end")
        ans = max(min(j-i+k-r,len(s)), ans)
        return ans