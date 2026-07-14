class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m-1
        xm = None

        while i<j and xm is None:
            a = (i+j)//2
            if matrix[a][0] == target:
                return True
            if matrix[a][0] < target:
                if matrix[a][-1] < target:
                    i = a+1
                else:
                    xm = a
            else:
                j = a-1

        if xm is None: xm = i
        print(xm)
        i = 0
        j = n-1
        if n == 1:
            return matrix[xm][0] == target
        elif n ==2:
            return target in matrix[xm]
        while i<j:
            a = (i+j)//2
            if matrix[xm][a] == target:
                return True
            if matrix[xm][a] < target:
                i = a+1
            else:
                j = a-1
        return matrix[xm][i]==target

