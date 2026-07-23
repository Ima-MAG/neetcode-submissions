class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalResult = []
        usedIndexes = []

        for index, word in enumerate(strs):
            if index in usedIndexes:
                continue

            group = [word]
            usedIndexes.append(index)
            sortedWord = sorted(word)

            for otherIndex, otherWord in enumerate(strs):
                if (otherIndex not in usedIndexes and sorted(otherWord) == sortedWord):
                    group.append(otherWord)
                    usedIndexes.append(otherIndex)

            finalResult.append(group)

        return finalResult