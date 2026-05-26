class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            res[key].append(words)

        return list(res.values())