class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapping = defaultdict(list)
        for i in range(len(groupSizes)):
            mapping[groupSizes[i]].append(i)

        res = []
        for key, value in mapping.items():
            arr = []
            for i in range(len(value)):
                arr.append(value[i])
                if len(arr) == key:
                    res.append(arr)
                    arr = []
        return res
