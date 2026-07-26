class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequences = {}
        for num in nums:
            if num in frequences:
                frequences[num] += 1
            else:
                frequences[num] = 1

        elementsSorted = sorted(frequences.keys(), key=lambda x: frequences[x], reverse=True)

        top_k = elementsSorted[:k]
        
        return top_k