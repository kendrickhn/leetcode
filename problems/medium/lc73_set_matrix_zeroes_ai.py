class Solution:
    def setZeroes(self, matrix):
        """
        Modifies matrix in place: if an element is 0, its entire row and column are set to 0.
        Constant extra space solution using first row/col as markers.
        """
        m, n = len(matrix), len(matrix[0])
        
        # Determine if first row or first column needs to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on markers in first row/col
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Finally zero out first row/col if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        # No return needed since we modify in place, but returning for convenience
        return matrix
