import cv2
import numpy as np

img1='images/breast_img1.png'
img2='images/breast_img3.png'
MSE_NUMERATOR = 1000.0
SIM_IMAGE_SIZE = (640, 480)
def get_image_similarity(img1, img2):
    # Converting to grayscale and resizing
    i1 = cv2.resize(cv2.imread(img1, cv2.IMREAD_GRAYSCALE), SIM_IMAGE_SIZE)
    i2 = cv2.resize(cv2.imread(img2, cv2.IMREAD_GRAYSCALE), SIM_IMAGE_SIZE)

    err = np.sum((i1.astype("float") - i2.astype("float")) ** 2)
    err /= float(i1.shape[0] * i2.shape[1])

    if err > 0.0:
        similarity = MSE_NUMERATOR / err
    else:
        similarity = 1.0
    return similarity

if __name__=='__main__':
    print(get_image_similarity(img1,img2))