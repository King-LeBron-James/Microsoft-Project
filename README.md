# Microsoft-Project
The project focuses on the gesture recognition 

This project is handling by Liu Jinyuan from UESTC, Wang Jiajun from SYSU and Chen Zhengpei from SYSU during our intern time in the Microsoft company.

Hello world !

#Part 2-Matching&Grading  by Wang Jiajun
The contours I get from my partners are binary images, so what I'm going to do is to match two contours and to grade. I've tried three methods, all from python-openCV.  
1.matchShapes --matchShapes.py
The method matchShapes is often used to compare two shapes or two contours, returing a value between 0 and 1. The smaller the value, the more similar two images are. And of cource, if the inputs are two same images, it will return 0.0. In this case, I use two gray images as inputs and record the results. What I find is that similar gestures can get a small value, however, different gestures may get a smaller value, maybe resulted from noise.  

2.padding  
An easy method to understand. I assume to pad one contour with another. By comparision of the area of the two contours, we may roughly get their similarity. To achieve this, cv2.contourArea is needed, whose inputs are required to be contours, a set of points. An existing method to get contours as the required form is cv2.findContours. But I found a new problem during my experiment. When this function is invoked, it may return several contours as a result of noise and break points in images. Now I try to connect the break points, making the contours consecutive. I refer to this blog https://blog.csdn.net/jyjhv/article/details/83863134  
For a single pixel, not at the boundary of the image, there are eight pixels around, which consist of its 'eight-neighbourhood'. Let's give a definition of "end point": for a point whose RGB is (255,255,255), if there is only one point whose RGB is (255,255,255) in its 'eight-neighbourhood', it is called an 'end point'. What to do next is to find all the 'end points', and if the distance between two 'end points' is smaller than a threshold, we use cv2.line to connnect them. Unfortunately, with the use of this algorithm, the contours detected do not decrease markedly, which means I have to give up this idea. For the algorithm, you can see connect.py.   

3.feature match -featureMatch.py  
When I search for imformation, I always include the key words 'contours matching', and the algorithms are limited. Now I'd like to try other algorithms not for 'contours matching', but for 'images matching'. Finally I decide to try a feature matching algorithm, the Brute-Force matching. I refer to this blog https://blog.csdn.net/u014281392/article/details/79693848  
There are many feature vectors in an image. For two vectors, the smaller the distance, the higher the similarity. The method cv2.BFMatcher.match can find N vector pairs that match if the distance between them is smaller than a certain threthold. For there is noise in our images, all feature vectors are not needed, so I choose M smallest distance pairs(M < N) and calculate the average distance of them. This value can serve as evaluation index for similarity. An interesting phenomenon is that we have different returning values for the same code, the same images on two different computers. But I haven't made it clear yet. To our content, the results are much better than before. Similar gestures can get a small value and different gestures always get a big value. We can match two gestures correctly by and large.  
As for grading, I set the interval 50 to 100, using an inverse scale function to map the average distance to a grade, which is transformed to integer.  
Above is my job. If you have any questions or advice, please contact me at 13539062145@163.com
