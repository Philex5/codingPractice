"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
leetcode 438
"""

import collections
import sys
class Solution:
    def findAnagrams(self, s: str, p: str) :
        """
        遍历一下，然后都排个序比较是否相等
        超出时间限制！！！
        :param s:
        :param p:
        :return:
        """
        if not s or not p:
            return []
        res = []
        for i in range(len(s) -len(p)+1):
            if sorted(p) == sorted(s[i:i+len(p)]):
                res.append(i)
        return res


    def findAnagrams1(self, s: str, p: str) :
        """
        字符串中的双指针解法
        有模板，可以套
        """
        res = []
        if len(p) > len(s):
            return res
        maps = collections.Counter(p)
        counter = len(maps.keys())
        begin, end = 0, 0,
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if s[begin] in maps:
                    maps[s[begin]] += 1
                    if maps[s[begin]] > 0:
                        counter += 1
                if end - begin == len(p):
                    res.append(begin)
                begin += 1












so = Solution()
print(so.findAnagrams('cbaebabacd', 'abc'))


