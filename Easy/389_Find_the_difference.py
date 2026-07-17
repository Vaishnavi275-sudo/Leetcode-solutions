from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        cos = Counter(s)
        cot = Counter(t)

        for ch in cot:
            if cos[ch] != cot[ch]:
                return ch