'''
Given an image represented by an N x N matrix,
 where each pixel in the image is represented by an integer,
 write a method to rotate the image by 90 degrees.
 Can you do this in place?
'''

# This is currently only swapping the corners of the matrix
# TODO - figure out how to increment to the other swaps
def rotateImage(matrix):
    r = c = 0
    n = len(matrix)
    for _ in range(n*n):
        temp = matrix[n-c][r]
        matrix[n-c][r] = matrix[r][c]
        r, c = n-c, r