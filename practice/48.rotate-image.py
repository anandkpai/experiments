#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix[0]) != len(matrix):
            raise ValueError('not a square, cannot rotate')
        
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] =  matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

# @lc code=end


if __name__ == '__main__':
    matrix = []
    matrix.append([1,2,3])
    matrix.append([4,5,6])
    matrix.append([7,8,9])

    s = Solution()
    
    s.rotate(matrix)
    print(matrix)