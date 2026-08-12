class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            number = nums[i]
            if number in seen:
                return True
            seen.add(number)
        return False