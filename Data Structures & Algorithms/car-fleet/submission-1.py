class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        current_fleet = 0

        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            arrive = (target - pos) / spd

            if arrive > current_fleet:
                count += 1
                current_fleet = arrive

        return count



