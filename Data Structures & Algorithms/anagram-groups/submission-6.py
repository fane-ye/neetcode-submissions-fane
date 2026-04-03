class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create char counter array
        hmap = defaultdict(list)
        for _str in strs:
            char_count = [0] * 26
            for _char in _str:
                pos = (ord(_char.lower()) - ord('a')) # 99 - 97 = 2 'c'
                char_count[pos] += 1
            hmap[tuple(char_count)].append(_str)

        return list(hmap.values())