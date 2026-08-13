class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            a = (left + right) // 2

            if nums[a] == target:
                return a
            elif nums[a] < target:
                left = a + 1
            else:
                right = a - 1

        return left