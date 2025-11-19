# згортка

#ЗНО(НМТ)
# математика -- 180
# укр мова -- 175
# англ мова -- 190

# коефіцієнти( важливість) -- вагами важливості
# математика -- 60%
# укр мова -- 10%
# англ мова -- 30%

# оцінку -- (180 + 175 + 190) / 3  середнє арифметичне
# оцінку -- 180*0.6 + 175*0.1 + 190*0.3 -- середнє зважене
# grades = [180, 175, 190]
# coefs = [0.6, 0.1, 0.3]

# згортка
import cv2
import utils
import numpy as np

# img = cv2.imread('data/lesson3/darken_page.jpg')

# # ядро згортки(фільтр, масив з коефіцієнтами)
# kernel = np.array(
#     [[0.1, 0.1, 0.1],
#      [0.1, 0.1, 0.1],
#      [0.1, 0.1, 0.1]]
# )
#
#
#
# kernel = np.array(
#     [[-1, -2, -1],
#      [0., 0., 0.],
#      [1, 2, 1]]
# )
#
# kernel = np.array(
#     [[-1, -2, -1],
#      [0., 0., 0.],
#      [1, 2, 1]]
# )
# res = cv2.filter2D(img, -1, kernel)
#
# cv2.imshow('res1', res)
#
# kernel = np.array(
#     [[-1, 0, 1],
#      [-2, 0., 2],
#      [-1, 0, 1]]
# )
#
#
# # згортка
# res = cv2.filter2D(img, -1, kernel)
#
# cv2.imshow('res', res)

# # застосування -- усунення шуму
# #img = utils.add_salt_and_pepper_noise(img, 0.001, 0.001)
# img = utils.add_gaussian_noise(img, 0, 5)
#
# # гаусове розмиття
# res = cv2.GaussianBlur(
#     img,
#     (13, 13),   # розмір ядра
#     2       # чим більше тим більше розвиття
# )
#
# # двосторонній фільтр
# res = cv2.bilateralFilter(
#     img,
#     d=9,  # розмір ядра
#     sigmaColor=75,   # наскільки зберігати різкість кольору
#     sigmaSpace=75,   # те ж саме що й в GaussianBlur
# )
#
# cv2.imshow('res', res)

# бінарізація

# зображення має бути чорно біле
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# проста бінарізація
# threshold = 5  # порогове значення
#
# res = gray.copy()
# mask = res > threshold
# res[mask] = 255
# res[~mask] = 0

# адаптивна бінарізація
# res = cv2.adaptiveThreshold(
#     gray,
#     255,  #  інтенчивність для білого кольору
#     cv2.ADAPTIVE_THRESH_MEAN_C,   # фурмула згортки(гаус)
#     cv2.THRESH_BINARY,    # це не чіпаємо
#     11,    # розмір ядра для згортки
#     2           # наскільки чутливою має бути бінарізація
# )
#
# cv2.imshow('res', res)
# cv2.imshow('original', img)
# cv2.waitKey(0)

# Завдання 1
# Відкрийте зображення data/lesson3/notes.png. Проведіть наступні дії:
#  проведіть бінарізацію(звичайну та адаптивну)
#  застосуйте розмиття(гаусове) візьміть ядра 3, 5, 11 та sigmaX 0, 2, 10
#  повторіть бінарізацію, але перед тим застосуйте bilateral filter

img = cv2.imread('data/lesson3/notes.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('original', img)


threshold = 100

res = img.copy()
mask = res > threshold
res[mask] = 255
res[~mask] = 0

cv2.imshow('bin', res)


res1 = cv2.adaptiveThreshold(
    img,
    255,  #  інтенчивність для білого кольору
    cv2.ADAPTIVE_THRESH_MEAN_C,   # фурмула згортки(гаус)
    cv2.THRESH_BINARY,    # це не чіпаємо
    13,    # розмір ядра для згортки
    4           # наскільки чутливою має бути бінарізація
)

cv2.imshow('GAUSS', res1)

res2 = cv2.GaussianBlur(
    img,
    (3, 3),   # розмір ядра
    2       # чим більше тим більше розвиття
)

cv2.imshow('GAUSS_blur', res2)

res3 = cv2.adaptiveThreshold(
    res2,
    255,  #  інтенчивність для білого кольору
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фурмула згортки(гаус)
    cv2.THRESH_BINARY,    # це не чіпаємо
    11,    # розмір ядра для згортки
    2           # наскільки чутливою має бути бінарізація
)

cv2.imshow('GAUSS_ad', res3)

bilateral = cv2.bilateralFilter(
    img,
    d=5,  # розмір ядра
    sigmaColor=75,   # наскільки зберігати різкість кольору
    sigmaSpace=75,   # те ж саме що й в GaussianBlur
)

cv2.imshow('bilateral', bilateral)

res4 = cv2.adaptiveThreshold(
    bilateral,
    255,  #  інтенчивність для білого кольору
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фурмула згортки(гаус)
    cv2.THRESH_BINARY,    # це не чіпаємо
    11,    # розмір ядра для згортки
    2           # наскільки чутливою має бути бінарізація
)

cv2.imshow('GAUSS1', res4)

cv2.waitKey(0)