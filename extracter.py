# import numpy as np
# import cv2 
# def extract_for_ground(img):
#     img = cv2.imread(img)
#     mask = np.zeros(img.shape[:2],np.uint8)
#     bgdModel = np.zeros((1,65),np.float64)
#     fgdModel = np.zeros((1,65),np.float64)

#     rect = (150,50,500,470)

#     cv2.grabCut(img,mask,rect,bgdModel,fgdModel,20,cv2.GC_INIT_WITH_RECT)
#     mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#     img = img*mask2[:,:,np.newaxis]
#     return img


from rembg import remove

from PIL import Image

def extract_for_ground(img):
    img = Image.open(img)
    output = remove(img)
    output.save("filtred.png")

extract_for_ground("./testimage/PLAGEAGADIR2.jpg")