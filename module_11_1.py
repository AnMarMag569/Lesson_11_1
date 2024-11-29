import numpy as np

#  массив из списка
my_array = np.array([1, 2, 3, 4, 5, 28, 56])
print(my_array,'\n')


# массив нулей размером 8x8
zeros_array = np.zeros((8, 8))
print(zeros_array, '\n')

# массив единиц размером 3x5
ones_array = np.ones((3, 5))
print(ones_array, '\n')

# Математические операции
# Сложение массивов
result_sum = my_array + 2
print(result_sum, '\n')

# Умножение массивов поэлементно
result_multiply = my_array * 2
print(result_multiply, '\n')

# Скалярное произведение векторов
vector1 = np.array([1, 2, 3, 8])
vector2 = np.array([4, 5, 6, 11])
dot_product = np.dot(vector1, vector2)
print(dot_product)