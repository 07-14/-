import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./cells.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((2,2), np.uint8)
erosion = cv2.erode(gray, kernel, iterations=3) # 腐蚀操作
dilation = cv2.dilate(erosion, kernel, iterations=3) # 膨胀
# cv2.imshow('processed img', dilation)
# cv2.waitKey()

# 画出直方图
plt.hist(gray.ravel(), 256, [0, 256])
plt.show()
# 二值化（阈值处理，二值法）
ret, thresh = cv2.threshold(dilation, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold img', thresh) # thresh就是我们要的阈值

# 开闭运算
thresh1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
thresh2 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

# 找出连通域
_, contours, hirearchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = [] # 建立空数组， 放连通域面积
contours1 = [] # 建立空数组，放减去最小面积的数字
for i in contours:
    area.append(cv2.contourArea(i))
    if cv2.contourArea(i) > 32:
        contours1.append(i)
print(len(contours1) - 1) # 计算连通域个数
draw = cv2.drawContours(img, contours1, -1, (0, 255, 0), 1)# 描绘连通域
# 求连通域中心，并在中心坐标描绘数字
for i, j in zip(contours1, range(len(contours1))):
    M = cv2.moments(i)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    # 在中心坐标描绘数字
    draw1 = cv2.putText(draw, str(j), (cX, cY), 1, 1, (255, 0, 255), 1)
# 展示图片
# cv2.imshow('result', draw1)
# cv2.waitKey()