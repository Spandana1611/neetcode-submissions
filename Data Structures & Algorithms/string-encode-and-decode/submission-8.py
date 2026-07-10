class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ['X'+str(len(i))+'X'+i for i in strs]
        return ''.join(s)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if len(s) == 2:
            return [""]
        
        ans = []
        i = 1
        j = ''
        while s[i]!='X':
            j+=s[i]
            i+=1
        if j=='': j = 0
        else: j =int(j)
        i+=1
        if i>= len(s):
            return ['']
        while i<len(s):
            while j==0 and i<len(s):
                ans.append('')
                i+=1
                if i<len(s): 
                    j = ''
                    while s[i]!='X':
                        j+=s[i]
                        i+=1
                    if j=='': j = 0
                    else: j =int(j)
                    i+=1
            st = ''
            while len(st)<j:
                st+=s[i]
                i+=1
            ans.append(st)
            i+=1

            if i<len(s): 
                j = ''
                while s[i]!='X':
                    j+=s[i]
                    i+=1
                if j=='': j = 0
                else: j =int(j)
                i+=1
                if i>=len(s):
                    ans.append('')
        return ans
