"""
颠倒给定的 32 位无符号整数的二进制位。

 

示例 1：

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
示例 2：

输入：11111111111111111111111111111101
输出：10111111111111111111111111111111
解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
      因此返回 3221225471 其二进制表示形式为 10101111110010110010011101101001。

leetcode 190

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bytes = [0] * 32
        i = 0
        while n > 0:
            b = n % 2
            n = n // 2
            bytes[31-i] = b
            i += 1
        print(bytes)
        bytes = bytes[::-1]
        print(bytes)
        res = 0
        for j in range(i):
            res += 2**(31-j) * bytes[j]
        return res

so = Solution()
print(so.reverseBits(13))



