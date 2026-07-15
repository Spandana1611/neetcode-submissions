import bisect

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d.keys():
            ex = self.d[key]
            self.d[key] = [ex[0] + [value], ex[1]+[timestamp]]
        else:
            self.d[key] = [[value], [timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d.keys():
            idx = bisect.bisect_right(self.d[key][1], timestamp)
            if idx == 0:
                return ""
            else:
                return self.d[key][0][idx-1]
        return ""