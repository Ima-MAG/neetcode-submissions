class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data: dict[str, list] = {}

        for i in strs:
            sortedWord = ''.join(sorted(i))
            if sortedWord not in data:
                data[sortedWord] = [i]
            else:
                data[sortedWord].append(i)

        return list(data.values())