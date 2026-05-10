class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_matrix = 0
        r_matrix = len(matrix) - 1

        while l_matrix <= r_matrix:
            mid_row = l_matrix + ((r_matrix - l_matrix) // 2)
            if target > matrix[mid_row][-1]:
                l_matrix = mid_row + 1
            elif target < matrix[mid_row][0]:
                r_matrix = mid_row - 1
            else:
                row = matrix[mid_row]
                break
        if l_matrix > r_matrix:
            return False

        l = 0
        r = len(row) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False