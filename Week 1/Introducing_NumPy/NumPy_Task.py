import numpy as np

# Генерация случайной матрицы
# Сгенерируйте матрицу, состоящую из 1000 строк и 50 столбцов,
# элементы которой являются случайными из нормального распределения N(1,100).
arr = np.random.normal(1, 10, (1000, 50))

# Нормировка матрицы
# Произведите нормировку матрицы из предыдущего задания:
# вычтите из каждого столбца его среднее значение,
# а затем поделите на его стандартное отклонение.
middle_int = np.mean(arr, 0)
standard_deviation = np.std(arr, 0)
arr_norm = (arr - middle_int) / standard_deviation

# Операции над элементами матрицы
# Выведите для заданной матрицы номера строк, сумма элементов в которых превосходит 10.
Z = np.array([[4, 5, 0],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])

Z_sum = np.sum(Z, 1)
print(np.nonzero(Z_sum > 10))


# Объединение матриц
# Сгенерируйте две единичные матрицы (т.е. с единицами на диагонали) размера 3x3.
# Соедините две матрицы в одну размера 6x3

A = np.eye(3)
B = np.eye(3)
print(np.vstack((A, B)))