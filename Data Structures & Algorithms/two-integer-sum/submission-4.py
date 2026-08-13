class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            number = nums[i]
            num = target - number
            if num in seen:
                return[seen[num], i]
            seen[number] = i 