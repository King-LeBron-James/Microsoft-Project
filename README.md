# Microsoft-Project
The project focuses on the gesture recognition 

This project is handling by Liu Jinyuan from UESTC, Wang Jiajun from SYSU and Chen Zhengpei from SYSU during our intern time in the Microsoft company.

Hello world !


1. Backgroud Information    
Attracting new members is the eternal theme of the gym, and the main means of capturing new members in today’s gyms is still delivering the leaflet, which has certain limitations, one of which is to limit the scope of the promotion. The general mobility of the staffs will not be particularly wide, so only customers in a particular area will know the information about the gyms. The second limitation is that the cost of ordinary leaflets is also quite high, and the gym needs to invest money to attract the employers who will deliever the leaflets. The efficiency of the staff, their three leaflets is also related to the professional conduct of the staff. Some staffs may throw all the leaflets, causing serious losses to the gym. So we propose to encourage the guests took pictures before our gym glasses and sent friends to attract new customers. The core of the project is that we need to be able to give the user a specific action profile. When the user are satisfied with their photos, they can take this photo and there is a grade which reflects the degree of similarities between the shape of users and the standard shape. 

2. Task Allocation    
For this project, we think there are three main tasks that we need to complete. The first is to extract the outline of the person, which means we should remove all kinds of complex backgrounds as well as noise, and then extract the shape of the outline. Then based on the need of further processing the contour, we should select the characteristics of the contour to carry out the contour matching, whether to select the similarity degree of the pixel point coordinates or directly detect the users' contour to the size of the specified contour ratio to judge. The third task is to design a matching scoring algorithm to score the user's actions. To finish this project faster, we decide to extract the contour of customer's hand and give the matching points firstly.


3. Extraction of Outline based on the Python (achieved by Liu Jinyuan)    
I firstly download the openCV package containing several useful image processing algorithms. Then I try to extract the contour of the hands of customers.  
(1)Firstly, I utilize some traditional image processing algorithms to extract the contour. By using VideoCapture function computer open the camera. And after reading the image, I used the Gaussian filter function GaussianBlur to smooth the pixels in the neighborhood of the image, in this case the pixels in different positions in the neighborhood are given different weight and thus the noise of image is filtered. Then I used the cvtColor function to convert the image to a grayscale one and used the threshold function to binarize the image. Finially, after demarcating the images, I used an advanced outline extraction algorithm called canny to extract the outline and the result is shown below:  
![1](https://github.com/King-LeBron-James/Microsoft-Project/blob/master/1.png)    
From the picture we can see that the canny edge extraction algorithm has a clearer extraction of the human contour, but the outline of the background is also extracted. The canny operator uses two different thresholds to detect strong and weak edges respectively. The larger threshold 2 is used to detect the obvious edges in the image, but in general the detection effect is not perfect and the edge detection is intermittent. Hence we should use the smaller first threshold to connect the edges of these discontinuities. Owing to this characteristics, the canny algrothim is very powerful and can detect the nuance edge. So I also thought of using the morphological opening and closing operations to eliminate the background points and lines in the image. The effect is as follows, which is still not ideal:The codes for this process is in the document called Extractmethod1.  
(2)
![2](https://github.com/King-LeBron-James/Microsoft-Project/blob/master/2.png)
