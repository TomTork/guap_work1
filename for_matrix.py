a = [[2, 4, 5], [6, 1, 1], [2, 2, 0], [7, 8, 3]]
b = [[1, 4, 7, 9], [3, 2, 1, 2], [8, 9, 10, 5]]


def transform_matrix(matrix: list):
    return list(zip(*matrix))


b = transform_matrix(b)
mm = []
time = []
for i in range(len(a)):
    time.clear()
    for t in range(len(a)):
        k = 0
        for y in range(len(a[0])):
            k += a[i][y] * b[t][y]
        time.append(k)
    mm.append(time.copy())
print(mm)
print(sum(mm[i][i] for i in range(len(mm))))
