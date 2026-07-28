class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data: dict[str, list] = {}

        for i in strs:
            sortedWord = ''.join(sorted(i))
            data.setdefault(sortedWord, []).append(i)

        return list(data.values())