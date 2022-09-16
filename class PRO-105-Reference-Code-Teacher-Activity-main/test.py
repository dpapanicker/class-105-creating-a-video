import cv2

#Use 0 for webcam
vid = cv2.VideoCapture(0)

#use the .isOpened() method which returns true ifVideoCapture() has worked successfully.
if(vid.isOpened()==False):
    print("Unable to read the feed")

# Let us extract some properties from our capture video frames via 
# Webcam:These properties of captured video frames are defined in OpenCV,
#  as these constant values:
# . Frame width
# . Frame height
# . Frames per second (fps).There are many video properties in OpenCV, 
# but we will limit our discussion with these three.
# cv2.CAP_PROP_FRAME_WIDTH
# .cv2.CAP_PROP_FRAME_HEIGHT
# .cv2.CAP_PROP_FPS 
# Properties of any video can be read using the get() method of
# the VideoCapture class. The values of the properties returned
# by the get() method will be as float values, that is, values
# decimal points. We can convert these values to integer numbers 
# using the int() method.
height  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

#As we can see in the Terminal, the height of video is 480 px,
# width 640 px, and it runs 30 frames per second(fps).After that it 
# displays a warning as it is not able to display the video.
# We know that a video consists of multiple frames, so to show the video
#  we need to first extract the frames of the video, then display the 
# individual frame as an image. We can use the read() method of the 
# VideoCapture class to display a video. At the beginning of this p
# rocess, it starts with the first frame. We will use a while loop so 
# that the vid.read()method will load every frame from the video file.

#Before we can understand how to read the video,let’s quickly understand
# Tuples data type in Python.Show the colab of tuples and explain.

#The read() method returns a tuple of two elements where:
# . The first element is a boolean. (Variable ret in the image below)
# . The second element is the actual video frame. 
# The variable ret and frame are user-defined. The value returned by the
#  read() method is assigned to ret, frame separately.
# When the first element is True, it indicates the video stream contains
#  a frame to read. As long as the value of ret is True it keeps on 
# reading the next frame. If the value is False, that means all the 
# frames of the video have been read.

#Let’s write a program to read and display video frames:
while(True):
      
    # Capture the video frame by frame
    ret, frame = vid.read()

    cv2.imshow("Web cam", frame)

#If any key is pressed, the corresponding ASCII code is assigned to 
# waitKey(). We can then take the desired action based on the key pressed

    if cv2.waitKey(25) == 32:
        break

vid.release() # vid.release() method to close the video.