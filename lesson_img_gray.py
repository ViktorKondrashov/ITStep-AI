# # дз завдання 3
# import numpy as np
#
# nums = np.array([1, 2, 3], dtype=np.uint8)
#
# # намагається помістити результат(типу float64) у ті самі
# # комірки(типу uint8) що не можливо -- error
# # nums *= 0.2
#
# # спочатку запускається nums * 0.2 -- створюється новий масив
# # далі запускається nums = ... -- змінюється вказівник
# nums = nums * 0.2
#
# print(nums)
# print(nums.dtype)
# import numpy as np
#
# # uint8 -- 0-255
#
# nums = np.array([2], dtype=np.uint8)
#
# res = nums - 10
# print(res)


# # # зображення у opencv
# import cv2
#
# # читання злображення
# img = cv2.imread(
#     'data/lesson1/cameraman.png',  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE # формат зображення
# )
#
#
# print(type(img))
# print(img)
# print(img.shape)
# print(img.dtype)
#
# # показати зображення
# cv2.imshow(
#     'image',   # назву
#     img
# )
#
#
# # зміна розміру зображення
# new_img = cv2.resize(img, (500, 500))
#
# # зміна у відсотках(на 50%)
# new_img = cv2.resize(img, None, fx=1.5, fy=1.5)
#
# cv2.imshow('resized_image', new_img)
# # програма чекає поки буде натиснута будь-яка кнопка
# cv2.waitKey(0)
# print('End')


# import utils
#
# utils.lesson1_image()

import cv2
import numpy as np

# читання злображення
img = cv2.imread(
    'data/lesson1/cameraman.png',  # шлях до файлу
    cv2.IMREAD_GRAYSCALE # формат зображення
)

img = cv2.resize(img, (500, 500))

# збільшення значення пікселів

cv2.imshow('original', img)

new_img = img.astype(np.int16)
new_img -= 80

# пікселів які опинились за межами діапазону 0-255
# треба повернути назад

# mask_255 = new_img > 255
# new_img[mask_255] = 255
# mask_0 = new_img < 0
# new_img[mask_0] = 0

# # те саме
# new_img = np.clip(new_img, 0, 255)
#
# new_img = new_img.astype(np.uint8)
#
# cv2.imshow('new', new_img)

# частина зображення з 200 по 400 рядок
segment = img[200:400]  # ті самі пікселі що і в img

cv2.imshow('segment', segment)

segment += 80

cv2.imshow('original', img)
cv2.imshow('segment', segment)

cv2.waitKey(0)

import cv2
import numpy as np
# Практичне завдання 1
# Відкрийте зображення data/Lenna.png. Виведіть на екран розмір зображення, тип даних,
# максимальну та мінімальну інтенсивність пікселів,
# саме зображення з підписом.
img = cv2.imread(
     'data/lesson1/Lenna.png',
     cv2.IMREAD_GRAYSCALE
)


new_img = cv2.resize(img, (500, 500))

print(type(new_img))
print(new_img)
print(new_img.shape)
print(new_img.dtype)

num_max = np.max(new_img)
num_min = np.min(new_img)

print(num_min)
print(num_max)

# Відкрийте зображення data/Lenna.png. Виведіть на екран такі зображень:
# Верхній лівий кут розміром 300х150

cut_img = new_img[0:300, 0:150]
cv2.imshow('left apper', cut_img)

# Центральний квадрат розміром 200х200
center = new_img[150:350, 150:350]
cv2.imshow('center', center)

# Верхню половину
half_up = new_img[0:250, :]
cv2.imshow('half up', half_up)


cv2.imshow('new', new_img)
cv2.waitKey(0)

# # Нижню половину
# half_bottom = new_img[250:, :]
# cv2.imshow('half_bottom', half_bottom)

# # Ліва половину
# half_left = new_img[:, :250]
# cv2.imshow('half_left', half_left)

# # права половину
# half_right = new_img[:, 250:]
# cv2.imshow('half_right', half_right)

# Завдання 3
# Відкрийте зображення data/Lenna.png. Створіть наступні
# зображення


# super_new_img = new_img.copy()
# super_new_img[:30, :] = 0
# super_new_img[-30:, :] = 255


# super_new_img = new_img.copy()
# super_new_img[:, :50] = 0
# super_new_img[:, -50:] = 0

super_new_img = new_img.copy()
super_new_img[:50, :] = 0
super_new_img[-50:, :] = 0
super_new_img[:, :50] = 0
super_new_img[:, -50:] = 0

cv2.imshow('new', new_img)
print(super_new_img)
cv2.imshow('super_new_img', super_new_img)



cv2.waitKey(0)

# Завдання 4
# Відкрийте зображення data/Lenna.png. Створіть маску для
# пік селів з інтенсивністю більше 128 та виведіть її. Також
# виведіть заперечення цієї маски.
# На оригінальному зображенні, усі пікселі які не
# відповідають масці замініть на 0 та виведіть результат

# mask = new_img > 128
# print(mask)
# print(mask.shape)
# print(mask.dtype)
#
# cv2.imshow('img', new_img)
#
# new_img[~mask] = 0
# cv2.imshow('new', new_img)
#
# new_img[mask] = 255
# cv2.imshow('new', new_img)

# mask = new_img > 128
#
# mask = mask.astype(np.uint8)
# print(mask)
# print(mask.shape)
# print(mask.dtype)
#
# mask = mask * 255
#
# cv2.imshow('mask', mask)


# cv2.waitKey(0)
#
# import utils
#
# @utils.trackbar_decorator(gamma_parameter=(1, 30))
# def gamma_correction(image, gamma_parameter):
#     gamma_parameter /= 10
#     result = 255 * (image/255) ** gamma_parameter
#     result = result.astype(np.uint8)
#
#     return result
#
#
# new_img = gamma_correction(img)
#
# cv2.imshow("edit_img", new_img)
# cv2.waitKey(0)