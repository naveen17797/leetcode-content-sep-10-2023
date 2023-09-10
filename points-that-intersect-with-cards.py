from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        intervals = self.merge_intervals(nums)
        points = 0
        for start, end in intervals:
            points += (end-start) + 1
        return points
    def merge_intervals(self, intervals):
        intervals.sort()
        stack = [intervals[0]]
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        return stack

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfPoints([[1,3],[5,8]]))
