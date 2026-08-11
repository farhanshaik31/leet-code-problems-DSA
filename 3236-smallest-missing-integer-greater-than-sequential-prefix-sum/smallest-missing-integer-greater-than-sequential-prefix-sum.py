
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seqsum = nums[0]

        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                seqsum += nums[j]
            else:
                break

        st = set(nums)

        while seqsum in st:
            seqsum += 1

        return seqsum