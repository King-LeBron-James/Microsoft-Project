import cv2
import numpy as np

def get_grades(values):
	grade = int(1/values)
	if grade<=20:#50~70
		grade+=50
	elif 20<grade and grade<=50:#70~76
		grade=int(66+grade/5)
	elif 50<grade and grade<=80:#76~88
		grade=int(56+grade/2.5)
	elif 80<grade and grade<=115:#88~95
		grade=int(72+grade/5)
	elif grade>115:#95~100
		grade = grade+grade/100
		if grade>100:
			grade=100
	return grade


def get_values():
	path = 'hands1\\hand'
	for i in range(1,13):
		for j in range(i+1,14):
			path1=path+ str(i) +'.png'
			path2=path+ str(j) +'.png'
			print('hand'+str(i)+' to '+'hand'+str(j)+':')
			img1 = cv2.imread(path1)
			img2 = cv2.imread(path2)
			img_gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)#转为灰度图像
			img_gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
			values = cv2.matchShapes(img_gray1, img_gray2, 1, 0.0)
			print('match  = ', values)
			print(get_grades(values))
			print('=========================================================')
"""
ret, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 
ret:和thresh相同； dst:结果图像
src:原图像 thresh:当前阈值 maxval:最大阈值，一般255 threshold type阈值类型
有以下几种：
enum ThresholdTypes {
    THRESH_BINARY     = 0, 二值图像，大于thresh的全设为maxval，其余设0
    THRESH_BINARY_INV = 1,
    THRESH_TRUNC      = 2,
    THRESH_TOZERO     = 3,
    THRESH_TOZERO_INV = 4,
    THRESH_MASK       = 7,
    THRESH_OTSU       = 8,
    THRESH_TRIANGLE   = 16
};
"""
get_values()
"""
在二值图像中找到轮廓
opencv3：
img,contours,hierarchy = cv2.findContours
(image, mode, method[, contours[, hierarchy[, offset ]]])  
我的opencv-python版本是4？
image是寻找轮廓的图像，即处理产生的dst
mode是检索模式
"""


