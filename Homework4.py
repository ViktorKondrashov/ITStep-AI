# Завдання 1
# Відкрийте зображення data\lesson2\darken.png. Проведіть з
# ним наступні операції, переведіть його в HSV формат та
# обробіть канал Value наступними способами:
#  застосуйте вирівнювання гістограм
#  збільшіть значення десь на 20-50%, оскільки тут
# результат буде типу float32 та явно вийде за межі [0-255]
# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)
# Виведіть результати обох обробок на екран

import numpy as np
import cv2

darken_orig = cv2.imread('data\lesson2\darken.png')
cv2.imshow('original', darken_orig)

darken_hsv = cv2.cvtColor(darken_orig, cv2.COLOR_BGR2HSV)

value = darken_hsv[:, :, 2]

new_value = cv2.equalizeHist(value)
darken_hsv[:, :, 2] = new_value

darken_new = cv2.cvtColor(darken_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('contrast_equalizeHist', darken_new)

darken_hsv1 = cv2.cvtColor(darken_orig, cv2.COLOR_BGR2HSV)

value1 = darken_hsv1[:, :, 2]
new_value1 = value1.astype(np.float32)

new_value1 *= 1.5 # на 50%
new_value1 = np.clip(new_value1, 0, 255)
new_value1 = new_value1.astype(np.uint8)

darken_hsv1[:, :, 2] = new_value1

darken_new1 = cv2.cvtColor(darken_hsv1, cv2.COLOR_HSV2BGR)

cv2.imshow('contrast_150%', darken_new1)

cv2.waitKey(0)






