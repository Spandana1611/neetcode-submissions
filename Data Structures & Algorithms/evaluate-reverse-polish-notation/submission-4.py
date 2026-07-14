class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        q = []
        for i in tokens:
            if i == '+':
                f = q[-1]+q[-2]
                q.pop()
                q.pop()
                q.append(f)
            elif i=='-':
                f = q[-2]-q[-1]
                q.pop()
                q.pop()
                q.append(f)
            elif i=='*':
                f=q[-2]*q[-1]
                q.pop()
                q.pop()
                q.append(f)
            elif i=='/':
                if q[-2]<0 or q[-1]<0:
                    f = (-1*q[-2])//q[-1]
                    f = -1*f
                else:
                    f=q[-2]//q[-1]
                q.pop()
                q.pop()
                q.append(f)
            else:
                q.append(int(i))
        return q[-1]