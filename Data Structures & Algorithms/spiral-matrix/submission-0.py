class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            #Go through first row
            if matrix:
                ret.extend(matrix.pop(0))

            if matrix and matrix[0]:
                for col in matrix:
                    ret.append(col.pop())

            if matrix:
                rev = matrix[-1][::-1]
                ret.extend(rev)
                matrix.pop()

            if matrix and matrix[0]:
                for i in range(len(matrix)):
                    ret.append(matrix[-i-1].pop(0))
            
        return ret

