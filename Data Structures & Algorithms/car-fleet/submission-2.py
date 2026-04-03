class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        res= sorted(zipped, key=lambda x: x[0], reverse=True)

        fleets = []
        for car in res:
            time = (target-car[0]) / car[1]
            print(time)
            if not fleets or time > fleets[-1]:
                fleets.append(time)
            
        return len(fleets)

        