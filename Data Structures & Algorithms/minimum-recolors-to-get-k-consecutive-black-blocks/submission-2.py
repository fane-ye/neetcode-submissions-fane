class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #create sliding window of size k
        #keep count of white blocks

            #if window size is reached update stae of min_ops
            #then move left pointer of window 
            #update the state of the window to reflect the moved left poiner

        min_ops = float('inf')
        count = defaultdict(int)
        l = 0
        for r in range(len(blocks)):
            count[blocks[r]] = count.get(blocks[r], 0) + 1

            if r - l + 1 == k and 'W' in count:
                min_ops = min(min_ops, count.get('W', 0))
                count[blocks[l]] -= 1
                l += 1

        return 0 if min_ops == float('infinity') else min_ops

            
        