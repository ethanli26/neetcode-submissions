class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = []
        flag = False
        for num in nums:
            if num in existing:
                flag = True
                break
            existing.append(num)

        return flag
