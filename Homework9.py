# Завдання 1
# Відкрийте відео data/lesson_pose/squat.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки. Отримайте координати 3-ох точок ноги
# Визначте кут між цими трьома точками. Скористайтесь функцією utils.get_angle(x1, y1, x2, y2, x3, y3) де x2, y2 – координати коліна(центральна точка)
# Запустіть відео та добавте на сам кадр кут згинання ніг.
# Визначіть нижню межу кута(якщо людина опустилась нижче вважаємо що вона достатньо опустилась) та верхню межу кута(якщо людина піднялась вище вважаємо що вона достатньо піднялась)
# Добавте кількість присідань та кут на кожен кадр.

import cv2
import ultralytics
import utils

model = ultralytics.YOLO('yolo11s-pose.pt')

orig_video = cv2.VideoCapture('data/lesson_pose/squat.mp4')

success, img = orig_video.read()

img = cv2.resize(img, None, fx=0.5, fy=0.5)

model_results = model.predict(img)
model_result = model_results[0]
plot_img = model_result.plot()

cv2.imshow('plot_img', plot_img)

cv2.waitKey(0)

move_down = True
counter = 0

while True:
    success, img = orig_video.read()

    if not success:
        break

    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    model_results = model.predict(img)
    model_result = model_results[0]
    keypoints = model_result.keypoints[0]
    xy = keypoints.xy

    right_hip = xy[0, 12]
    x_right_hip = right_hip[0]
    y_right_hip = right_hip[1]

    right_knee = xy[0, 14]
    x_right_knee = right_knee[0]
    y_right_knee = right_knee[1]

    right_foot = xy[0, 16]
    x_right_foot = right_foot[0]
    y_right_foot = right_foot[1]

    angle = utils.get_angle(x_right_hip, y_right_hip, x_right_knee, y_right_knee, x_right_foot, y_right_foot)

    if angle <= 90 and move_down:
        move_down = False
        counter += 0.5

    if angle >= 170 and not move_down:
        move_down = True
        counter += 0.5

    cv2.putText(
        img,                  # зображення
        f'Counter: {counter}, Angle: {angle}',    # текст
        (20, 20),     # верхний левый угол
        cv2.FONT_HERSHEY_SIMPLEX,    # шрифт
        0.8,          # розмір шрифту(відсоток до стандарту)
        (255, 255, 255),      # колір у bgr(тут чорний)
        2           # товщина ліній
    )

    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
