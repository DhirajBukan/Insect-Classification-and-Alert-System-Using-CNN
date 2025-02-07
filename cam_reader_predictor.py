import cv2
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
from twilio.rest import Client
        
saved = load_model('/home/pi/Desktop/7april5classes.h5')

vid = cv2.VideoCapture(0)
#print(vid.get(cv2.CAP_PROP_AUTO_EXPOSURE))
#r=vid.set(cv2.CAP_PROP_EXPOSURE,1)
#print(r)
#print(vid.get(cv2.CAP_PROP_EXPOSURE))
#time.sleep(2)
ret, frame = vid.read()
#print(ret)
#cv2.imshow('frame', frame)
cv2.imwrite("/home/pi/Desktop/img.png",frame)
vid.release()
# Destroy all the windows
#cv2.destroyAllWindows()
classes_indices = {0:'Assassins Bug', 1:'Bee', 2:'Mosquito', 3:'Moths', 4:'Wasp'}
img = image.load_img('/home/pi/Desktop/img.png')
#plt.imshow(img)
#plt.show()
img = img.resize((64,64))
#plt.imshow(img)
#plt.show()
X = image.img_to_array(img)
X = np.expand_dims(X,axis = 0)
images = np.vstack([X])
pred = saved.predict(images)
print(pred)
#saved.summary()
print(max(pred[0]))
count = 0
for i in pred[0]:
    
    if int(i) == 1:
        print(classes_indices[count])
       
        

        # Find these values at https://twilio.com/user/account
        # To set up environmental variables, see http://twil.io/secure
        account_sid = ''
        auth_token = ''

        client = Client(account_sid, auth_token)

        client.api.account.messages.create(
            to="",
            from_="",
            body=f"{classes_indices[count]} Detected By The System In Your Area.")
        print(classes_indices.values())
    count = count + 1
