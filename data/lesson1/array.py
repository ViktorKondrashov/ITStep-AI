import numpy as np

# # створення масиву
# array = np.array([1, 2, 3, 4, 5])
#
# print(array)
# print(array.shape)  # розмір масиву
# print(array.dtype)  # тип даних в одній комірці масиву
#
# # двовимірний масив(таблиця/матриця)
# array = np.array([[1, 2, 3, 4, 5],
#                   [6, 7, 8.5, 9, 10]])
#
# print(array)
# print(array.shape)  # розмір масиву
# print(array.dtype)  # тип даних в одній комірці масиву


# # порівнння швидкості для масивів та списків
# import time
#
#
# N = 10_000_000
# nums_list = list(range(N))
# nums_array = np.array(range(N))
#
# start = time.time()
# res = sum(nums_list)
# end = time.time()
#
# print(f"Python list: {end - start:0.5f} sec")
#
# start = time.time()
# res = np.sum(nums_array)
# end = time.time()
#
# print(f"Numpy array: {end - start:0.5f} sec")


# завжди використовувати функції numpy
# цикл for -- це велике зло

# # створення та розміри
#
# nums = np.arange(10, 20, 2)  # масив з діапазону, як в range
# print(nums)
#
# nums = np.zeros(shape=(3, 4))  # масив з нулів
# print(nums)
#
# # змінити розмір масиву
# nums = np.arange(10, 20)
# new_nums = nums.reshape((2, 5))
# print(new_nums)
# print(new_nums.shape)

# індексація
# nums = np.arange(10, 20)
#
# print(nums)
# # print(nums[2])
# # print(nums[2:5])  # зріз з 2(включно) по 5(не включно)
# # print(nums[2:7:2])  # зріз з 2(включно) по 7(не включно) крок 2
# # print(nums[:3])    # перші 3
# # print(nums[-3:])  # останні 3
#
# nums[2] = 0
#
# #nums[2:7] = 0
# nums[2:7] *= -1
#
# print(nums)

# nums = np.array([[1, 2, 3, 4, 5],
#                   [6, 7, 8.5, 9, 10]])
#
# print(nums.shape)  # рядки, стовпчики
# # для двовимірних масивів йже 2 індекса -- рядка та стовпчика
#
# print(nums[1, 2])    # 8.5
# print(nums[1])       # рядок з індексом 1
# print(nums[1, 2:4])  # рядок з індексом 1, стовпчики з 2 по 4
# print(nums[0:2, 1:4])  # блок рядки з 0 по 2 та стовпчики з 1 по 4
# print(nums[:, 3])    # стовпчик 3
#
# nums[0:2, 1:4] += 100
# print(nums)

# булеві маски
# nums = np.array([[1, 20, 3, 4, 5],
#                    [6, 7, 8.5, 9, 10]])
#
# mask = nums > 7
#
# print(mask)
# print(mask.dtype)
#
# print(nums[mask])  # дістати числа які відповідають масці(умові)
#
# nums[mask] = 0
# print(nums)
#
# # дістати числа які не відповідають масці(умові)
# # and -- &
# # or  -- |
# # not -- ~
# print(nums[~mask])
#
# # кількість чисел що білше 7
# print(np.sum(mask))

# Завдання 1
# Створіть масив з числами від 1 до 10. Виведіть його, його розмір, тип даних.
# Змініть розмір масиву на (5, 2). Знову виведіть масив, розмір та тип даних

new_array = np.arange(1, 11)
print(new_array)
print(new_array.shape)
print(new_array.dtype)

print(type(new_array.shape))

new_array1 = new_array.reshape(5, 2)
print(new_array1)
print(new_array1.shape)
print(new_array1.dtype)

new_array1 += 2
print(new_array)
print(new_array1)