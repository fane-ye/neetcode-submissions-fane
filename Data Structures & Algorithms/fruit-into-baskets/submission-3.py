class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxF = 0

        n = len(fruits)
        for i in range(n):
            fruit_types = set() #1, 2, 3 
            fruit_count = 0
            for j in range(i, n):
                fruit_types.add(fruits[j])
                fruit_count += 1

                if len(fruit_types) <= 2:
                    maxF = max(maxF, fruit_count)
                else:
                    continue

            print("")
        return maxF
                    


        