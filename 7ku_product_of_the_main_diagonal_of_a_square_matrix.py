'''
Description:

Given a list of rows of a square matrix, find the product of the main diagonal.

Examples:

main_diagonal_product([[1,0],[0,1]]) => 1

main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) => 45
'''
def main_diagonal_product(mat):
    #TODO
    sum = 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                sum *= mat[i][j]
    return sum