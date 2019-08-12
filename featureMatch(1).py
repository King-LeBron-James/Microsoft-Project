import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab

def get_grades(value):
    grade = int(50+(50/value))
    if grade > 100:
        grade = 100
    return grade

def get_values():
	path = 'hands\\hand'
	for i in range(1,13):
		for j in range(i+1,14):
			path1=path+ str(i) +'.png'
			path2=path+ str(j) +'.png'
			print('hand'+str(i)+' to '+'hand'+str(j)+':')
			img1 = cv2.imread(path1)
			img2 = cv2.imread(path2)
			img_gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)#转为灰度图像
			img_gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
			print(cv2.contourArea(img_gray1))
			print('match  = ', cv2.matchShapes(img_gray1, img_gray2, 1, 0.0))
			print('=========================================================')

def featureMatchP():
	path='hands1\\hand'
	for i in range(1,13):
		for j in range(i+1,14):
			path1=path+str(i)+'.png'
			path2=path+str(j)+'.png'
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
			#plt.show()
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
			#plt.show()
			#匹配：遍历两幅图像的特征描述符[包含特征点信息的向量]然后计算向量之间的距离
			bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
			matches = bf.match(des1,des2)
			matches = sorted(matches, key = lambda x:x.distance)
			avg = 0.0
			for k in range(0,50):
				avg=avg+matches[k].distance
			print('hand'+str(i)+' to '+'hand'+str(j)+':')
			print(len(matches))
			avg=avg/len(matches)
			print(avg)
			print(get_grades(avg))
			print('============================================')

def featureMatch(pathA,pathB):
    standard=cv2.imread(pathA)
    img=cv2.imread(pathB)
    grayScale1=cv2.cvtColor(standard,cv2.IMREAD_GRAYSCALE)
    grayScale2=cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)
	#展示原图q
    plt.figure()
    plt.axis('off')
#    plt.imshow(hand1)
    plt.figure()
    plt.axis('off')
#    plt.imshow(hand2)
	#plt.show()
	#特征提取
    orb=cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(grayScale1, None)
    kp2, des2 = orb.detectAndCompute(grayScale2, None)
    print(type(des1))
    print(type(des2))
	#可视化特征点
#    keypoint1 = cv2.drawKeypoints(image=hand1, outImage=hand1,keypoints=kp1,flags=4, color=(0,255,0))
#    keypoint2 = cv2.drawKeypoints(image=hand2, outImage=hand2,keypoints=kp2,flags=4, color=(0,255,0))
    plt.figure()
    plt.axis('off')
#    plt.imshow(keypoint1)
    plt.figure()
    plt.axis('off')
#    plt.imshow(keypoint2)
	#plt.show()
	#匹配：遍历两幅图像的特征描述符[包含特征点信息的向量]然后计算向量之间的距离
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key=lambda x:x.distance)
    avg = 0.0
    for k in range(0,60):
        avg=avg+matches[k].distance
#    print('hand'+str(i)+' to '+'hand'+str(j)+':')
    avg=avg/len(matches)
    c=get_grades(avg)
    print('Your grade is:',c)
    return c

camera = cv2.VideoCapture(0) # 参数0表示第一个摄像头
bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
while True:
    grabbed, frame_lwpCV = camera.read()
#    res_b = do_contours('hands1\\hand4.png')
#    print('res_b %d contours' % len(res_b))
    fgmask = bs.apply(frame_lwpCV) # 背景分割器，该函数计算了前景掩码
    # 二值化阈值处理，前景掩码含有前景的白色值以及阴影的灰色值，在阈值化图像中，将非纯白色（244~255）的所有像素都设为0，而不是255
    th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    # 下面就跟基本运动检测中方法相同，识别目标，检测轮廓，在原始帧上绘制检测结果
    dilated = cv2.dilate(th, es, iterations=2) # 形态学膨胀
    edgeC=cv2.Canny(dilated,100,255)
    cv2.imshow("canny", edgeC)
    standard = cv2.imread("C:/Users/Dell/hand4.png")
    cv2.imshow("standard",standard)
#    print('match A-B = ', cv2.matchShapes(res_a[0], res_b[0], 1, 0.0))
#    for c in contours:
#        if cv2.contourArea(c) > 1600:
#            (x, y, w, h) = cv2.boundingRect(c)
#            cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (255, 255, 0), 2)
#    cv2.imshow('mog', fgmask)
#    cv2.imshow('thresh', th)
#    cv2.imshow('detection', frame_lwpCV)


    if cv2.waitKey(1) & 0xFF == ord('q'):   #如果按下q 就截图保存并退出
         cv2.imwrite("C:/Users/Dell/customer.png", edgeC)   #保存路径
         break
#    if Grade>70:
#        cv2.imwrite("C:/Users/Dell/Pictures/Saved Pictures/results.png", edgeC)
#        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
Grade=featureMatch("C:/Users/Dell/hand4.png","C:/Users/Dell/customer.png")
