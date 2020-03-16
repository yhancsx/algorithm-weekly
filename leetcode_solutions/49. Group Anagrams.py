class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))
            dic[ss].append(s)

        return dic.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for s in strs:
            count = [0] * 28
            for c in s:
                count[ord(c) - ord('a')] += 1

            dic[tuple(count)].append(s)

        return dic.values()