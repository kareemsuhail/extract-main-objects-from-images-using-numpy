## import numpy as np is a convention
import numpy as np
## we need matplotlib just to read and show data
from matplotlib import pyplot as plt
from math import sqrt
'''
defining cut off function which takes 3 parameters :
1.image: which the image that we will draw over it ( image path as String)
2.mask : the image that we want to cut off ( image path as String)
3.power : which the percent for color difference ( float from 0 to 1) 
note that the default value for power is 0.2 
'''
def cutOff(image,mask,power=0.2):
    # reading both image and mask and converting them into numpy array
    image_np = np.array(plt.imread(image))
    mask_np  = np.array(plt.imread(mask))
    # note that the shape of these arrays will be :
    # ( image height,image width ,3)
    # note that 3 is constant since we are dealing with RGB image
    mask_background = mask_np[1, 1]
    # this is our reference vector  which we will use to measure difference 
    # according to it 
    start_row = image_np.shape[0] - mask_np.shape[0]
    start_col = image_np.shape[1] - mask_np.shape[1]
    # this part is just to define where should we start printing our 
    # mask over the original image ,, here we will use the right coroner as a start 
    #==============================================
    # now we want to iterate over each pixel and measure the difference 
    # then we want to calculate the percentage of difference so it is easy for us 
    # as humans to figure out if we need this pixel or not 
    # as you see we will start iterating over the mask 
    for row in range(start_row, image_np.shape[0]):
        for col in range(start_col, image_np.shape[1]):
            # reading pixel from mask
            temp_RGB_vector = mask_np[row - start_row, col - start_col]
            # measuring distance
            temp_distance = (np.sum(np.absolute(np.subtract(temp_RGB_vector.astype(np.int16), mask_background.astype(np.int16)))))
            # calculating percentage
            percent = temp_distance / sqrt((255) ** 2 + (255) ** 2 + (255) ** 2)
            # if the percent is lower than desired power do not write this pixel over
            # original image
            if percent < power:
                continue
            # if not write is
            for color in range(3):
                image_np[row, col, color] = mask_np[row - start_row, col - start_col, color]
    # Read the image from 3d numpy array it and show it
    plt.imshow(image_np)
    plt.show()
# let us test our code
cutOff("captain-america.jpg","geeks.jpg",0.4)