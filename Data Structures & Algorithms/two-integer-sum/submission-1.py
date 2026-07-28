class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        counter = 0

        for i in nums:
            k = target - i
            if k in myDict.keys() and i + k == target and counter != myDict[k]:
                r = [myDict[k], counter]
                r.sort()
                return r
            myDict[i] = counter
            counter += 1