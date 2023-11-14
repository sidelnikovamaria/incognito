def is_magic (matrix):
    Summ = sum(matrix[0])
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
            if temp != Summ or sum(matrix[i]) != Summ:
                return False
            return True
mat = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))
mat = [[4, 3, 4], [3, 4, 3], [3, 3, 4]]
print(is_magic(mat))
