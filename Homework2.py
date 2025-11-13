import numpy as np

# Завдання 1
# Створіть масив:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Використовуючи індекси виведіть:
# ● число 14
# ● третій рядок
# ● перший стовпчик
# ● верхню половину
# ● замініть числа в рядках 2-3 на 100
# ● зробіть другий рядок таким як останній рядок

nums = np.arange(1, 17)
nums = nums.reshape(4, 4)

print(nums)
print(nums[3, 1])
print(nums[2])
print(nums[:, 0])
print(nums[0:2])

nums[1] = 100
nums[2] = 100
print(nums)

nums[1] = nums[-1]
print(nums)

print()

# Завдання 2
# У масиві з попереднього завдання створіть маску для
# парних чисел. З її допомогою
# ● виведіть самі числа
# ● замініть їх на 100

nums = np.arange(1, 17)
nums = nums.reshape(4, 4)

mask = nums % 2 == 0

print(mask)
print(nums[mask])

nums[mask] = 100
print(nums)

print()

# Завдання 3
# Створіть 2 масиви типу uint8:
# Масив 1: 128 200 10
# Масив 2: 250 10 34
# Об’єднайте їх у пропорції 20% першого масив + 80%
# другого масиву. В результаті має бути тип даних uint8 та
# числа в діапазоні 0-255

nums1 = np.array([128, 200, 10], dtype=np.uint8)
nums2 = np.array([250, 10, 34], dtype=np.uint8)

print(nums1)
print(nums2)

nums = nums1 / 5 + nums2 * 0.8
nums = nums.astype(np.uint8)
print(nums)

