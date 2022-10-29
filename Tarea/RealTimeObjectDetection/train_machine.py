import cv2
import os
import time
import uuid
 
IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

signs_to_learn = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_images = 15

for sign in signs_to_learn: 
    !mkdir {'Tensorflow/workspace/images/collectedimages\\'+ sign}
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(sign))
    time.sleep(5)
    for imgnum in range(number_images):
        ret,frame = cap.read()
        imagename = os.path.join(IMAGES_PATH,sign,sign+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitKey(1) && 0xFF == ord('q'):
            break
    cap.release()

