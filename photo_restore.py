#importing libraries
import cv2, argparse, numpy as np, os

def sliding_windows(gray):
    windows=[]
    #image dimensions
    height,width=gray.shape
    #calculating height and width of window


    #sliding


#function to restore image
def restore(imagepath):
    #checking if file exists
    assert os.path.exists(imagepath), 'The image does not exists.'
    #reading image
    image=cv2.imread(imagepath)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    sliding_windows(gray)

#main
if __name__=='__main__':
    #argument
    #parser=argparse.ArgumentParser()
    #parser.add_argument('--i','-imagepath',type=str,required=True,help='path to the image.')
    #args=parser.parse_args()
    #restoring image
    #restore(args.imagepath)
    restore('.\\1.jpg')