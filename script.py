#author: Tarun Pathak
#--------------------

#importing packages
#------------------
import cv2

#preprocessing logic
#-------------------
def preprocess(image):
    #converting to grayscale
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #returning image
    return gray

#function to create mask
#mask is a binary image (single channel) where non-zero areas
#are used for inpainting
#---------------------------
def get_mask(image):
    #preprocessing the image
    gray=preprocess(image)
    #getting brightest and dimmest pixel
    min,max,minLoc,maxLoc=cv2.minMaxLoc(gray)
    thresh_low= .7 * max
    print(f'Dimmest Pixel: {int(min)}\nBrightest Pixel: {int(max)}\nThreshold for binary image: {int(thresh_low)}')
    #returning threshold image
    #minimum thresh limit will be average of brightest and dimmest pixel
    ret, image = cv2.threshold(gray,thresh_low, max, cv2.THRESH_BINARY)
    return image

#main
#----
if __name__=='__main__':
    #reading image
    img=cv2.imread('.\\samples\\2.jpg')
    #getting mask
    mask=get_mask(img)
    #correcting image
    corrected_image = cv2.inpaint(img, mask, 50, cv2.INPAINT_NS)
    cv2.imshow('Original', img)
    cv2.imshow('Corrected', corrected_image)
    cv2.waitKey(0)
