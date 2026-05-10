class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_pairs = []
        for i in range(len(position)):
            sorted_pairs.append([position[i], speed[i]])
        
        sorted_pairs.sort(reverse=True)

        for i in range(len(sorted_pairs)):
            car_pos = sorted_pairs[i][0]
            car_speed = sorted_pairs[i][1]
            time = (target - car_pos) / car_speed
            if not stack or stack[-1] < time:
                stack.append(time)
            
        
        return len(stack)