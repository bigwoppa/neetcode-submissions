class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            number = nums[i]
            if number in seen:
                return True
            seen[number] = i
        return False