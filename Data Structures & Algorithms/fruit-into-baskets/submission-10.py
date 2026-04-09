class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        fruitC = 0
        maxF = 0
        l = 0
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            fruitC += 1
            while len(basket) > 2:
                print("basket too big, basket: ", basket)
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                fruitC -= 1
                l += 1
            maxF = max(maxF, fruitC)
        return maxF





            

        