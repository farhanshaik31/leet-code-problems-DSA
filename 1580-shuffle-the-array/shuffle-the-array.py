class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        half = []
        for i in range(n,len(nums)):
            half.append(nums[i])
        for i in range(n):
            res.append(nums[i])
            res.append(half[i])
        return res
