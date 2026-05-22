class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        # build prefix
        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
                continue
            if height[i] > prefix[i - 1]:
                prefix[i] = height[i]
            else:
                prefix[i] = prefix[i - 1]

        # tracing prefix
        # [0,2,0,3,1,0,1,3,2,1]
        # [0,2,2,3,3,3,3,3,3,3]

        # build suffix
        for i in range(len(height) - 1, -1, -1):
            if i == (len(height) - 1):
                suffix[i] = height[i]
                continue
            if height[i] > suffix[i + 1]:
                suffix[i] = height[i]
            else:
                suffix[i] = suffix[i + 1]

        # tracing suffix
        # [0,2,0,3,1,0,1,3,2,1]
        # [3,3,3,3,3,3,3,3,2,1]


        # [0,2,2,3,3,3,3,3,3,3] prefix
        # [3,3,3,3,3,3,3,3,2,1] suffix

        # calculate water using prefix and suffix
        total_water = 0
        for i in range(len(height)):
            water_at_i = min(prefix[i], suffix[i]) - height[i]

            if water_at_i > 0:
                total_water += water_at_i

        return total_water