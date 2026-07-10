class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = []
        small = []
        caps = []
        for i in range(ord('0'), ord('9')+1): nums.append(i)
        for i in range(ord('a'), ord('z')+1): small.append(i)
        for i in range(ord('A'), ord('Z')+1): caps.append(i)
        valid_ch = nums + small + caps
        s1 = ''
        for i in s:
            o = ord(i)
            if o in valid_ch :
                if o in caps:
                    ch = chr(o-caps[0]+small[0])
                    s1+=ch
                else: s1+=i
        i = 0
        j = len(s1) - 1
        while i<j:
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True