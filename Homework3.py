# Завдання 1
# Відкрийте зображення data/Lenna.png. Прочитайте маски data/mask1.png та data/mask2.png.
# Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or() та виведіть результат
# Виведіть ту частину зображення, яка відповідає:
#  mask1
#  mask2
#  mask1 і mask2
# Усі пікселі які не відповідають маскам замінити на 0, перед застосуванням змініть тип даних у масці на bool

import cv2
import numpy as np

img = cv2.imread("data/lesson1/Lenna.png", cv2.IMREAD_GRAYSCALE)
mask1 = cv2.imread("data/lesson1/mask1.png", cv2.IMREAD_GRAYSCALE)
mask2 = cv2.imread("data/lesson1/mask2.png", cv2.IMREAD_GRAYSCALE)

mask = cv2.bitwise_or(mask1, mask2)

cv2.imshow('mask', mask)

mask1 = mask1.astype(bool)
mask2 = mask2.astype(bool)
mask = mask.astype(bool)

img1 = img.copy()
img1[~mask1] = 0

cv2.imshow('img1', img1)

img2 = img.copy()
img2[~mask2] = 0

cv2.imshow('img2', img2)

img3 = img.copy()
img3[~mask] = 0

cv2.imshow('img3', img3)

cv2.waitKey(0)

# Завдання 2
# Домашнє завдання
# Виведіть зображення(мабуть data/lesson1/baboo.jpg?). Підберіть самостійно межі

img = cv2.imread("data/lesson1/baboo.jpg", cv2.IMREAD_GRAYSCALE)

cut_img = img[12:48, 60:196]
cv2.imshow('cut_img', cut_img)

cv2.waitKey(0)



