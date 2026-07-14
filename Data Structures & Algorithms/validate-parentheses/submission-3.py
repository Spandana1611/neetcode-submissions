class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for i in s:
            if i in ['(', '{', '[']:
                q.append(i)
            elif i == ')':
                if len(q)==0 or q[-1]!='(':
                    return False
                q.pop(len(q)-1)
            elif i == '}':
                if len(q)==0 or q[-1]!='{':
                    return False
                q.pop(len(q)-1)
            else:
                if len(q)==0 or q[-1]!='[':
                    return False
                q.pop(len(q)-1)
        return len(q) == 0

