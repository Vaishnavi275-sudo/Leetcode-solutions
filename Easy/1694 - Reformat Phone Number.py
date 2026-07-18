class Solution(object):
    def reformatNumber(self, number):

        digits = []

        # Keep only digits
        for ch in number:
            if ch.isdigit():
                digits.append(ch)

        ans = []
        i = 0
        n = len(digits)

        while n - i > 4:
            ans.append("".join(digits[i:i+3]))
            i += 3

        if n - i == 4:
            ans.append("".join(digits[i:i+2]))
            ans.append("".join(digits[i+2:i+4]))
        else:
            ans.append("".join(digits[i:]))

        return "-".join(ans)