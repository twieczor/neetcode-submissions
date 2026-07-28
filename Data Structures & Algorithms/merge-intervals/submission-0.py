class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)

        if n < 2:
            return intervals

        intervals.sort(key = lambda p: p[0])

        ret = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1,n):
            if intervals[i][0] > end:
                ret.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif intervals[i][1] > end:
                end = intervals[i][1]

        
        ret.append([start, end])

        return ret

