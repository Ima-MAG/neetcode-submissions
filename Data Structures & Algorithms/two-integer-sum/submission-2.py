class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        counter = 0

        for i in nums:
            k = target - i
            if k in myDict:
                return [myDict[k], counter]
            myDict[i] = counter
            counter += 1