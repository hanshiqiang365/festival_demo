#author:hanshiqiang365

import cv2

img_photo = cv2.imread('photo.jpg')
img_moon = cv2.imread('moon.png')

w_photo, h_photo = img_photo.shape[:2]
w_moon, h_moon = img_moon.shape[:2]

scale = w_photo / w_moon / 4

img_moon = cv2.resize(img_moon, (0, 0), fx=scale, fy=scale)
w_moon, h_moon = img_moon.shape[:2]

for c in range(0, 3):
    img_photo[w_photo - w_moon:, h_photo - h_moon:, c] = img_moon[:, :, c]

cv2.imwrite('new_photo.jpg', img_photo)

