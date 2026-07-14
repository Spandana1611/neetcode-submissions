class MinStack:

    def __init__(self):
        self.l = []
        self.m = None

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.m == None and len(self.l) == 1:
            self.m = val
        elif self.m != None:
            self.m = min(self.m, val)

    def pop(self) -> None:
        if self.m == self.l[-1]:
            self.m = None
        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        if self.m is not None:
            return self.m
        else:
            return min(self.l)
        
