class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        k = list(s)
        left = 0
        right = len(k) - 1

        while left < right:
            pair = min(k[left], k[right])
            k[left] = pair
            k[right] = pair

            left += 1
            right -= 1

        return "".join(k)