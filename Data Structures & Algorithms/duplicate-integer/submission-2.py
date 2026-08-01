class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}

        for i, num in enumerate(nums):
            if num in myDict:
                return True
            myDict[num] = i

        return False