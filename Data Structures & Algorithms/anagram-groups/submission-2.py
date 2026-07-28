class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        data: dict[str, list] = {}

        for i in strs:
            sortedWord = ''.join(sorted(i))
            if not sortedWord in data:
                data[sortedWord] = [i]
            else:
                data[sortedWord].append(i)

        res = list(data.values())

        return res