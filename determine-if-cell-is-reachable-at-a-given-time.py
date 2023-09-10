class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1: return False
        return max(abs(fy - sy), abs(fx - sx)) <= t


if __name__ == '__main__':
    s = Solution()
    print(s.isReachableAtTime(870744264, 360311537, 820090827, 890107308, 274809225))
