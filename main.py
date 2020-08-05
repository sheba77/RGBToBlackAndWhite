import sys
import numpy as np
from imageio import imread, imwrite
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import sys

# Write a function which reads an image file and converts it into a given representation
# read_image(filename, representation)

GRAY_SCALE = 2
FULL_COLOR = 3
FULL_SIZE = 255


# this function gets an image and a number:
# if the image is gray scaled then if 1 will return the image ( 2 is not a valid param)
# if the image is colorful then if 1 will return gray scale and if 2 will return original

def read_image(filename, representation):
    im = imread(filename)  # read file
    float_im = im.astype(np.float64)/FULL_SIZE #change to float 64

    if len(im.shape) == GRAY_SCALE:  # if is gray scale
        if representation == GRAY_SCALE:
            print("this cant happen")
    elif len(im.shape) == FULL_COLOR:  # if is not gray scale
        if representation == '1':
            float_im = rgb2gray(float_im)
    return float_im


# uses rea_image function
# The function should open a new figure and display the loaded image in the converted representation
def imdisplay(filename, representation):
    im = read_image(filename, representation)
    plt.figure()
    if len(im.shape) == GRAY_SCALE:
        #if img is grayscaled
        plt.imshow(im, cmap=plt.cm.gray)
    elif len(im.shape) == FULL_COLOR:
        #if is not gray scaled
        plt.imshow(im)
    plt.axis("off")
    plt.show()

#transform an RGB image into the YIQ
def rgb2yiq(imRGB):
    # color_matrix = np.matrix(imRGB[:, :, 0], imRGB[:, :, 1], imRGB[:, :, 2])
    M = np.array([[0.299, 0.587, 0.114], [0.596, -0.275, -0.321], [0.212, -0.523, 0.311]])
    return np.dot(imRGB, M.T)


# def yiq2rgb(imYIQ):

# imdisplay(sys.argv[1], sys.argv[2])
im = imread(sys.argv[1])


im = ex1.read_image(sys.argv[1], sys.argv[2])
im = (im*255).round().astype(np.uint8)
imwrite("temp_im.jpg", im)
