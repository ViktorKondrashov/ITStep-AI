# сегментація зображень
import ultralytics
import numpy as np
import cv2

# # модель для сегментації
# model = ultralytics.YOLO('yolo11s-seg.pt')
#
# img = cv2.imread('data/lesson_seg/human.jpg')

# # застосування моделі
# # results -- list з результами для кожного зображення в predict
# results = model.predict(
#     img,
#     # conf=0.5,
#     # iou=0.1
# )
#
# # дістати результати для першого(єдиного) зображення
# result = results[0]
#
# # візуалізація результату
# res_img = result.plot(
#     boxes=True,   # чи показувати рамки(boxes)
#     masks=True,    # чи показувати маски сегментації(boxes)
# )
#
# # маски об'єктів
# masks = result.masks.data
# # print(masks)
# # print(masks.shape)  # (кількість об'єктів, висота, ширина)
#
# # класи об'єктів
# cls = result.boxes.cls
# print(cls)
#
# # назви класів
# names = result.names
# print(names)
#
# # де знаходиться людина
# idx = 0
# # маска людини
# mask = masks[idx]
# # print(mask)
# # print(mask.shape)
#
# # переведення маски у формат opencv
# mask = mask.cpu()   # відключення від графічного процесора
# mask = mask.numpy() # переведення у масив numpy
# mask = mask.astype(np.uint8)   # зміна типу даних
# mask *= 255         # заміна 1 на 255 щоб було видно
#
#
# # print(mask)
# # print(mask.dtype)
# # print(np.unique((mask)))  # унікальні значення в масиві


# # відео
# cap = cv2.VideoCapture(0)
#
# # зображення фону
# background_img = cv2.imread('data/lesson4/canal.png')
# cv2.imshow('background', background_img)
#
# # зміна розміру зображення з фоном
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#
# background_img = cv2.resize(background_img, (width, height))
#
# while True:
#     success, img = cap.read()
#
#     if not success:
#         break
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     # застосувати модель
#     results = model.predict(img)
#     result = results[0]
#
#     res_img = result.plot()
#
#     # маска
#     masks = result.masks.data
#     mask = masks[0]
#     mask = mask.cpu()
#     mask = mask.numpy()
#     mask = mask.astype(np.uint8)
#     mask *= 255
#
#     # добавити фон
#     mask_bool = mask.astype(bool)
#
#     # заміна пікселів які не людина
#     img[~mask_bool] = background_img[~mask_bool]
#
#     cv2.imshow('res', res_img)
#     cv2.imshow('mask', mask)
#     cv2.imshow('original', img)

    # print(f'{img.shape = }')
    # print(f'{mask.shape = }')
    # print(f'{background_img.shape = }')

# cv2.imshow('mask', mask)
# cv2.imshow('result', res_img)
# cv2.imshow('original', img)
# cv2.waitKey(0)

#  Завдання 1
# Відкрийте зображення data/lesson_seg/crop3.jpg  Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/crop-seg.jpg
# Покажіть усі маски рослин з підписами назви цієї
# рослини.  Покажіть також самі рослини, для цього застосуйте
# маску, і всі зайві пікселі замініть на 255(зробити білий фон)

import ultralytics
import numpy as np
import cv2

model = ultralytics.YOLO('data/lesson_seg/crop-seg.pt')

img = cv2.imread('data/lesson_seg/crop3.jpg')

cv2.imshow('original', img)

results = model.predict(
    img
    )

result = results[0]

res_img = result.plot(
    boxes=True,
    masks=True
)

cv2.imshow('segments', res_img)

# Покажіть усі маски рослин з підписами назви цієї рослини.
names = result.names
print(names)

masks = result.masks.data
print(masks[0])

# print(mask)

cls = result.boxes.cls
print(cls)

nums = len(cls)

heigh, width, _  = img.shape
# print(heigh, width)

for i in range(nums):
    name = names[int(cls[i])]

    mask = masks[i]
    mask = mask.numpy()
    mask = mask.astype(np.uint8)
    mask *= 255
    mask = cv2.resize(mask, (width, heigh))

    # cv2.imshow(f'{name}, {i}', mask)
    # print(mask.shape)

    mask_bool = mask.astype(bool)
    img_current = img.copy()
    img_current[~mask_bool] = 255

    cv2.imshow(f'{name}, {i}', img_current)


#
# print(img.shape)

cv2.waitKey(0)

# Завдання 2
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення
# Порахуйте розмір кожної рослини(площа маски)
# Покажіть найбільшу рослину кожного виду
# Практичне завдання

# модель для сегментації
model = ultralytics.YOLO('data/lesson_seg/crop-seg.pt')

img = cv2.imread('data/lesson_seg/crop3.jpg')

results = model.predict(img)
result = results[0]
masks = result.masks.data

print(masks)
print(masks.shape)

area = masks.sum(dim=[1,2])
print(area)

index_max_area = area.argmax()
print(index_max_area)


