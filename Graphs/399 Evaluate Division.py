from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = {}

        def find(root: str):
            if root not in mapping:
                mapping[root] = (root, 1)
            gid, w = mapping[root]
            if gid != root:
                new_gid, new_w = find(gid)
                mapping[root] = (new_gid, w * new_w)
            return mapping[root]

        def union(a: str, b: str, w: float):
            a_id, a_w = find(a)
            b_id, b_w = find(b)
            if (a_id != b_id):
                mapping[b_id] = (a_id, a_w * w / b_w)

        for i in range(0, len(equations)):
            union(equations[i][0], equations[i][1], values[i])

        res = []
        for q in queries:
            if q[0] not in mapping or q[1] not in mapping:
                res.append(-1.0)
                continue
            s_id, s_w = find(q[0])
            t_id, t_w = find(q[1])
            if s_id != t_id:
                res.append(-1.0)
            else:
                res.append(1 / s_w * t_w)

        return res

