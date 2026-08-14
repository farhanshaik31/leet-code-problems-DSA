class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        right = 0
        maxlength = 0
        while right < len(s):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1
            while freq[ch] > 2:
                freq[s[left]] -= 1
                left += 1
            count = right - left + 1
            maxlength = max(maxlength, count)
            right += 1

        return maxlength