# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transp_matrix(x: list, y: list):
    len_array = 0
    for e in x:
        if len(e) > len_array: len_array = len(e)
    for i in range(len_array):
        temp_list = []
        for j in range(len(x)):
            if i >= int(len(x[j])): temp_list.append(None)
            else: temp_list.append(x[j][i])
        y.append(temp_list)
    return y


w = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0]]
a = []

print(transp_matrix(w, a))




