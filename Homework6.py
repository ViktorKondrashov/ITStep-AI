# Завдання 1
# Відкрийте відео з файлу data\lesson7\meter.mp4. Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через bilateralFilter

import cv2

cap = cv2.VideoCapture('data\lesson7\meter.mp4')

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    'new_meter.mp4',  # шлях до файлу
    fourcc,        # кодек
    fps,
    (width, height),
    isColor=False   # чи кадри кольорові
)


while True:
    success, img = cap.read()

    if not success:
        break

    res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.GaussianBlur(res, (9, 9), 1)

    res = cv2.bilateralFilter(res, 7, 75, 75)

    res = cv2.adaptiveThreshold(res,
                                255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,
                                23,
                                2
                            )

    # cv2.imshow('orig', img)
    cv2.imshow('res', res)

    writer.write(res)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
writer.release()