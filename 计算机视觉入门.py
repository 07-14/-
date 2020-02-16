import cv2
import numpy as np
"""
B,G,R
"""

# # 颜色翻转
# src = cv2.imread('./fea.png') # 读取彩色图片
# img_info = src.shape
# image_h = img_info[0]
# image_w = img_info[1]
# dst = np.zeros((image_h, image_w, 3), np.uint8)
#
#
# for i in range(image_h):
#     for j in range(image_w):
#         (b, g, r) = src[i][j]
#         dst[i][j] = (255-b, 255-g, 255-r)
#
# cv2.imshow('src', src)
# cv2.waitKey()
# cv2.imshow('2', dst)
# cv2.waitKey()


# 浮雕效果
img = cv2.imread('./fea.png') # 读取彩色图片
img_info = img.shape

image_h = img_info[0]
image_w = img_info[1]
image_c = img_info[2]
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img=np.zeros((image_h,image_w,3),dtype=np.uint8)

for i in range(image_h):
    for j in range(image_w-1):
        current_Pixel = int(img[i,j])
        next_Pixel = int(img[i, j+1])
        new_Pixel = current_Pixel - next_Pixel + 150
        # 阈值处理
        if new_Pixel > 255:
            new_Pixel = 255
        if new_Pixel < 0:
            new_Pixel = 0
        new_img[i, j] = new_Pixel
cv2.imshow('new_img',new_img)
cv2.waitKey()
cv2.destroyAllWindows()