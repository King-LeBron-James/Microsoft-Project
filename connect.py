"""
将不连续的轮廓接起来
断点修补的方法时判断两个端点的距离是否小于一个阈值，如果小于该阈值则将两个端点连接
断点的定义：相邻8点只有一个rgb值为(255,255,255)
详见https://blog.csdn.net/jyjhv/article/details/83863134
效果并不好，不论是轮廓多的(不清晰、噪声)还是轮廓少的(清晰，如hand4.png只有两个)
都不能有效地减少轮廓的数量，从而使用contourArea函数计算面积
"""
import cv2
import numpy as np
import math
from PIL import Image

def linkContours():
    src=cv2.imread('hands1\\hand1.png')
    srcMat=np.asarray(src,dtype='float64')#转为3维数组，表示第(i,j)位置的rgb值为(a,b,c)
    #但是在二值图像中，a,b,c只能是全0或者全255
    pointxy=[]
    for i in range(1,len(srcMat)-1):
        dataPre = srcMat[i-1]
        dataCurr = srcMat[i]
        dataNext = srcMat[i+1]
        for j in range(1,len(srcMat[i])-1):
            p1 = dataCurr[j]
            if (p1 == (0,0,0)).all():#tuple的比较逻辑要加上.all()或者.any()
                continue
            p2 = dataPre[j]
            p3 = dataPre[j + 1]
            p4 = dataCurr[j + 1]
            p5 = dataNext[j + 1]
            p6 = dataNext[j]
            p7 = dataNext[j - 1]
            p8 = dataCurr[j - 1]
            p9 = dataPre[j - 1]
            if (p2+p3+p4+p5+p6+p7+p8+p9 == (255,255,255)).all():
                ptPoint = (j,i)
                pointxy.append(ptPoint)
    print(pointxy)
    threshold = 30 #门限，两个端点的距离小于它，则将它们连起来
    for i in range(0,len(pointxy)-1):
        for j in range(i+1,len(pointxy)):
            dx = pointxy[i][0] - pointxy[j][0]
            dy = pointxy[i][1] - pointxy[j][1]
            distance = math.sqrt(dx*dx+dy*dy)
            print(distance)
            if distance < threshold:
                cv2.line(srcMat,pointxy[i],pointxy[j],(255,255,255),1)
    new_im = Image.fromarray(srcMat.astype(np.uint8))
    print(type(new_im))
    new_im.save('hands2\\4.png')


linkContours()



