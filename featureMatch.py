"""
特征匹配法之Brute-Force
利用matches函数计算特征向量之间的距离
计算匹配对之间的距离的平均值（前50），以此衡量匹配程度
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab

def get_grades(value):
	return int(50+50/value)

def featureMatch():
	path1='hand.png'
	path2='hand2.png'
	hand1=cv2.imread(path1)

	grayScale1=cv2.cvtColor(hand1,cv2.IMREAD_GRAYSCALE)
	hand2=cv2.imread(path2)
	grayScale2=cv2.cvtColor(hand2,cv2.IMREAD_GRAYSCALE)
	#展示原图
	plt.figure()
	plt.axis('off')
	plt.imshow(hand1)
	plt.figure()
	plt.axis('off')
	plt.imshow(hand2)
	plt.show()
	#特征提取
	orb=cv2.ORB_create()
	kp1, des1 = orb.detectAndCompute(grayScale1, None)
	kp2, des2 = orb.detectAndCompute(grayScale2, None)
	#可视化特征点
	keypoint1 = cv2.drawKeypoints(image=hand1, outImage=hand1,keypoints=kp1,
                              flags=4, color=(0,255,0))
	keypoint2 = cv2.drawKeypoints(image=hand2, outImage=hand2,keypoints=kp2,
                              flags=4, color=(0,255,0))
	plt.figure()
	plt.axis('off')
	plt.imshow(keypoint1)
	plt.figure()
	plt.axis('off')
	plt.imshow(keypoint2)
	plt.show()
	#匹配：遍历两幅图像的特征描述符[包含特征点信息的向量]然后计算向量之间的距离
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = bf.match(des1,des2)
	matches = sorted(matches, key = lambda x:x.distance)
	avg = 0.0
	for k in range(0,50):
		avg=avg+matches[k].distance
	#print('hand'+str(i)+' to '+'hand'+str(j)+':')
	print(len(matches))
	avg=avg/len(matches)
	print(avg)
	print(get_grades(avg))
	print('============================================')


featureMatch()


