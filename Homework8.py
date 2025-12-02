# Завдання 1
# Відкрийте зображення data/lesson_seg/tumor1.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/brain-tumor-seg.jpg
# Визначте площу пухлини в пікселях.
# Визначте площу в
# (1 піксель – 0,0025
# )
# В залежності від площі присвойте пухлині певний тип
#  <10 – small
#  10-25 – middle
#  >25 – large
# Покажіть пухлину – за допомогою маски усі лишні
# пікселі зробіть 0, а як назву зображення використайте її тип

import ultralytics
import numpy as np
import cv2

model = ultralytics.YOLO('data/lesson_seg/brain-tumor-seg.pt')

img = cv2.imread('data/lesson_seg/tumor1.jpg')

cv2.imshow('original', img)

results = model.predict(img)

result = results[0]

res_segm = result.plot()

cv2.imshow('segments', res_segm)

masks = result.masks.data

area = masks.sum(dim=[1,2])

area_tumor = area.item() * 0.0025
print(area_tumor)

if area_tumor > 25:
    type_tumor = 'large'
elif area_tumor >= 10:
    type_tumor = 'middle'
else:
    type_tumor = 'small'

mask = masks[0]
mask = mask.numpy()
mask_bool = mask.astype(bool)

img_res = img.copy()
img_res[~mask_bool] = 0

cv2.imshow(type_tumor, img_res)

cv2.waitKey(0)
