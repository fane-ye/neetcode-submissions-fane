class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create char counter array
        bitmaps = []
        for _str in strs:
            char_count = [0] * 26
            for _char in _str:
                pos = (ord(_char.lower()) - ord('a')) # 99 - 97 = 2 'c'
                char_count[pos] += 1
            bitmaps.append(char_count)

        # add maps to a hash table
        hmap = {}
        for i in range(len(strs)):
            _bitmap = tuple(bitmaps[i])
            if _bitmap not in hmap:
                hmap[_bitmap] = []
            hmap[_bitmap].append(strs[i]) # add str to map


        return list(hmap.values())