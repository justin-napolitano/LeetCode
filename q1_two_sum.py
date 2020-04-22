class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for i, j in enumerate(nums):
            remaining = target - j
            if remaining in passed:
                return [passed[remaining], i]
            passed[j] = i
        return []
            