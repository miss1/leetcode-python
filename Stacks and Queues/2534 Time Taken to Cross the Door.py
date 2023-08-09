"""
simulation
两个queue，记录enter，exit里等待的人
"""

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        # 0: enter, 1: exit, default: 1
        i, time, direction = 0, arrival[0], 1
        arr = [collections.deque(), collections.deque()]
        res = [0] * len(arrival)
        while (i < len(arrival)):
            if (arrival[i] <= time):
                arr[state[i]].append(i)
                i += 1
            else:
                if len(arr[0]) == 0:
                    direction = 1
                elif len(arr[1]) == 0:
                    direction = 0
                if len(arr[direction]) > 0:
                    res[arr[direction].popleft()] = time
                time += 1
        while (len(arr[direction]) > 0):
            res[arr[direction].popleft()] = time
            time += 1
        direction = 0 if direction == 1 else 1
        while (len(arr[direction]) > 0):
            res[arr[direction].popleft()] = time
            time += 1
        return res

