class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, des = set(), set()
        for path in paths:
            f, t = path
            start.add(f)
            if f in des:
                des.remove(f)
            if t not in start:
                des.add(t)
        return ', '.join(map(str, des))
