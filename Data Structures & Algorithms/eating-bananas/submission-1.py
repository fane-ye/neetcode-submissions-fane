class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        curr_max = 0
        curr_min = float('inf')
        for i in range(len(piles)): #n
            lo = 1
            hi = piles[i]

            while lo <= hi: #logM
                mid = (lo+hi)//2
                can_eat_all = self.canEatAll(piles, h, mid)

                if can_eat_all is True:
                    curr_min = min(curr_min, mid)
                    hi = mid - 1
                elif can_eat_all is False:
                    lo = mid + 1
            
        return curr_min

    def canEatAll(self, piles, h, k):
        time = 0
        for n in piles:
            time = time + n//k + (1 if n%k else 0)
        print("time: ", time,"k: ", k)
        return True if time <= h else False


        




        