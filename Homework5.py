# Завдання 1
# Відкрийте зображення data/lesson3/sonet.png. Проведіть бінарізацію.
# Обов’язково використайте:
#  розмиття або наведення різкості
#  адаптивну бінарізацію
#  очищеня шумів

import cv2
import numpy as np

img = cv2.imread(r'data/lesson3/sonet.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("original", img)

res = cv2.GaussianBlur(
    img,
    (3, 3),   # розмір ядра
         2       # чим більше тим більше розмиття
 )

cv2.imshow("GaussBlur", res)

res1 = cv2.adaptiveThreshold(
     img,
     255,  #  інтенчивність для білого кольору
     cv2.ADAPTIVE_THRESH_MEAN_C,   # формула згортки(гаус)
     cv2.THRESH_BINARY,    # це не чіпаємо
     7,    # розмір ядра для згортки
     3          # наскільки чутливою має бути бінарізація
 )

cv2.imshow('adapt_bin', res1)

# # двосторонній фільтр
res2 = cv2.bilateralFilter(
     img,
     d=3,  # розмір ядра
     sigmaColor=75,   # наскільки зберігати різкість кольору
     sigmaSpace=75,   # те ж саме що й в GaussianBlur
)

cv2.imshow("bil_filter", res2)

cv2.waitKey(0)