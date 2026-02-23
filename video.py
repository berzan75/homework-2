import os
import cv2
from PIL import Image

path=os.chdir("C:\\Users\\berza\\OneDrive\\Documenten\\cv\\video using images\\images")

mean_height=0
mean_width=0

number_of_images=len(os.listdir('.'))

for i in os.listdir('.'):
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    mean_width=mean_width+width
    mean_height=mean_height+height

mean_width=mean_width//number_of_images
mean_height=mean_height//number_of_images
print(mean_width,mean_height)

for i in os.listdir('.'):
    if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png'):
        img=Image.open(os.path.join(path,i))
        width,height=img.size
        print(height,width)
        image_resize=img.resize((mean_width,mean_height),Image.ANTIALIAS)
        image_resize.save(i,"JPEG",quality=95)
def video_generator():
    video_name="video.avi"
    os.chdir("C:\\Users\\berza\\OneDrive\\Documenten\\cv\\video using images\\images")
    images=[]
    for i in os.listdir('.'):
        if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png'):
            images.append(img)