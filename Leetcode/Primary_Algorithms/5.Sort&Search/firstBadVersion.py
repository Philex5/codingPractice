"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 2:
        return True
    return False


class Solution:
    # 确定中间的案例是否是错误案例，在确定是往前还是往后查找
    def firstBadVersion(self, n):
        if n == 1:
            return 1
        p = n // 2
        if isBadVersion(p):
            n = p
            while isBadVersion(n):
                if n == 1:
                    if isBadVersion(n):
                        return 1
                    else:
                        return p
                n -= 1
            return n
        else:
            n = p + 1
            while not isBadVersion(n):
                n += 1
            return n

so = Solution()
print(so.firstBadVersion(4))