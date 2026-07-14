class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s_idx = []
        ans = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            # print(s_idx, i)
            while len(s_idx)>0 and temperatures[s_idx[-1]] < temperatures[i]:
                # print(ans, s_idx)
                ans[s_idx[-1]] = i-s_idx[-1]
                s_idx.pop()
            s_idx.append(i)
        return ans
