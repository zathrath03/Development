from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        while timestamp > 0:
            if timestamp in self.time_map:
                if value := self.time_map.get(timestamp).get(key):
                    break
            timestamp -= 1
        else:
            return ""
        return value


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.set("foo2", "bar3", 2)
timeMap.get("foo", 1)
timeMap.get("foo", 3)
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)
timeMap.get("foo", 5)
print("hello")
