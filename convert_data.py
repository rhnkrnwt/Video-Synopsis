import os
import pickle
import numpy as np

IMG_HEIGHT = 288
IMG_WIDTH = 352
PIXELS = IMG_HEIGHT * IMG_WIDTH

def convert_rgb_numpy(img, pickled_image):
    img_data = np.ndarray((3, IMG_HEIGHT, IMG_WIDTH))
    with open(img, "rb") as rgb_file:

        byte_data = rgb_file.read()
        int_data = [i for i in byte_data]
        r = np.array(int_data[:PIXELS])
        g = np.array(int_data[PIXELS:2*PIXELS])
        b = np.array(int_data[2*PIXELS:3*PIXELS])
        
        img_data[0] = np.array(r.reshape((IMG_HEIGHT,IMG_WIDTH)))
        img_data[1] = np.array(g.reshape((IMG_HEIGHT,IMG_WIDTH)))
        img_data[2] = np.array(b.reshape((IMG_HEIGHT,IMG_WIDTH)))

        with open(pickled_image, "wb") as img_p:
            pickle.dump(img_data, img_p)

def convert_all_images(img_directory, pickled_directory):
    for file in os.listdir(img_directory):
        img = img_directory + file
        pickled_image = pickled_directory+file+".p"

        if not os.path.exists(pickled_image):
            convert_rgb_numpy(img, pickled_image)


img_directory = "/Users/Sai/Desktop/VideoSynopsis/CSCI576ProjectMedia/Image/RGB/"
pickled_directory = "/Users/Sai/Desktop/VideoSynopsis/CSCI576ProjectMedia/Image/RGB_Pickled/"

convert_all_images(img_directory, pickled_directory)
