# import cv2
# import os
# import numpy as np

# input_folder = "faulty_images"
# output_folder = "faulty_cropped"

# os.makedirs(output_folder, exist_ok=True)

# MARGIN = 150


# def detect_blue_edges(image):

#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     lower_blue = np.array([90, 80, 80])
#     upper_blue = np.array([130, 255, 255])

#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     h, w = mask.shape

#     column_sum = np.sum(mask, axis=0)

#     blue_columns = np.where(column_sum > h * 20)[0]

#     if len(blue_columns) == 0:
#         return None, None

#     left = blue_columns[0]
#     right = blue_columns[-1]

#     return left, right


# for file in os.listdir(input_folder):

#     if not file.lower().endswith((".jpg", ".jpeg", ".png")):
#         continue

#     path = os.path.join(input_folder, file)

#     img = cv2.imread(path)

#     if img is None:
#         print("Failed:", file)
#         continue

#     h, w = img.shape[:2]

#     left, right = detect_blue_edges(img)

#     if left is None:
#         print("Blue background not detected:", file)
#         continue

#     left = max(left + MARGIN, 0)
#     right = min(right - MARGIN, w)

#     cropped = img[:, left:right]

#     save_path = os.path.join(output_folder, file)

#     cv2.imwrite(save_path, cropped)

#     print("Cropped:", file)

# print("Done ✅")




# import cv2
# import os

# input_folder = "faulty_images"
# output_folder = "faulty_cropped"

# os.makedirs(output_folder, exist_ok=True)

# MARGIN = 1000   # controls how much body to keep

# # Load face detector
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# for file in os.listdir(input_folder):

#     if not file.lower().endswith((".jpg",".jpeg",".png")):
#         continue

#     path = os.path.join(input_folder, file)

#     img = cv2.imread(path)

#     if img is None:
#         print("Failed:", file)
#         continue

#     h, w = img.shape[:2]

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(60,60)
#     )

#     if len(faces) == 0:
#         print("Face not detected:", file)
#         continue

#     x,y,fw,fh = faces[0]

#     center_x = x + fw//2

#     left = max(center_x - MARGIN, 0)
#     right = min(center_x + MARGIN, w)

#     cropped = img[:, left:right]

#     save_path = os.path.join(output_folder, file)

#     cv2.imwrite(save_path, cropped)

#     print("Cropped:", file)

# print("Done ✅")





import cv2
import os

input_folder = "faulty_images"
output_folder = "faulty_cropped"

os.makedirs(output_folder, exist_ok=True)

MARGIN = 1000

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

for file in os.listdir(input_folder):

    if not file.lower().endswith((".jpg",".jpeg",".png")):
        continue

    path = os.path.join(input_folder, file)

    img = cv2.imread(path)

    if img is None:
        print("Failed:", file)
        continue

    h, w = img.shape[:2]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60,60)
    )

    if len(faces) == 0:
        print("Face not detected:", file)
        continue

    x,y,fw,fh = faces[0]

    center_x = x + fw//2

    # horizontal crop
    left = max(center_x - MARGIN, 0)
    right = min(center_x + MARGIN, w)

    # better head crop
    top = max(int(y - fh * 0.7), 0)

    cropped = img[top:h, left:right]

    save_path = os.path.join(output_folder, file)

    cv2.imwrite(save_path, cropped)

    print("Cropped:", file)

print("Done ✅")