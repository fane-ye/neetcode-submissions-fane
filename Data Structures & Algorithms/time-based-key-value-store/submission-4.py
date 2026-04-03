VAL = 0
TIME = 1
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #i need a data structure where one key can store multiple values
        # but also those values need to be kept in a stricly increasing order
        # i must also store the timestamp it was inserted

        #hashmap, where key is key, then the value is a stack ds, with a tuple storing value and timestamp

        self.store[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        #return the value at the timestamp if prev_timestamp ==
        #or return the next highest prev_timestamp value

        if key not in self.store:
            return ""
        vals = self.store[key]
        
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp < vals[mid][TIME]:
                r = mid - 1
            elif timestamp > vals[mid][TIME]:
                l = mid + 1
            else:
                return vals[mid][VAL]
        
        if l == 0:
            return ""
        return vals[l - 1][VAL]