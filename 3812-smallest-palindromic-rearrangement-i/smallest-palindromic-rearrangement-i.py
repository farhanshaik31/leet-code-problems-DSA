class Solution:
    def smallestPalindrome(self, s: str) -> str:
        k = sorted(s)
        left = []
        mid = ""

        i = 0
        while i < len(k):
            count = k.count(k[i])

            left.append(k[i] * (count // 2))

            if count % 2 == 1:
                mid = k[i]

            i += count

        left = "".join(left)
        right = left[::-1]

        return left + mid + right