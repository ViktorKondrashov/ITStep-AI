# Завдання 1
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть параметри
# Можете змінити розмір кадру для кращої візуалізації cv2.resize()

import ultralytics
import cv2

model = ultralytics.YOLO('yolov8s.pt')

cap = cv2.VideoCapture('data\lesson8\meetings.mp4')
success, img = cap.read()

img = cv2.resize(img, None, fx=0.25, fy=0.25)

cv2.imshow('original', img)

results = model.predict(
    img,
    conf=0.25,
    iou=0.7
)

result = results[0]

names = result.names
print(names)

# самі об'єкти
cls = result.boxes.cls
print(cls)

# візуалізація результатів
res_img = result.plot()
cv2.imshow('result', res_img)

cv2.waitKey(0)


# Завдання 2
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та почніть показувати відео з моменту, коли людей стало 5

cap = cv2.VideoCapture('data\lesson8\meetings.mp4')

# відео
while True:
    success, img = cap.read()

    if not success:
        break

    img = cv2.resize(img, None, fx=0.25, fy=0.25)

    results = model.predict(img)
    result = results[0]

    cls = result.boxes.cls
    list_cls = cls.tolist()
    if list_cls.count(0) < 5:
        continue

    cv2.imshow('video_5_person', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

