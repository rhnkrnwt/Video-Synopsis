import os
import pickle
import cv2
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def read_pickled_image(pickled_image):
    with open(pickled_image, "rb") as img_p:
        img_data = pickle.load(img_p)
        return img_data        


def load_images(pickled_directory):
    images = dict()
    for file in os.listdir(pickled_directory):
        with open(pickled_directory+file, "rb") as img_p:
            img_data = pickle.load(img_p)
            images[file] = img_data
    return images

def display_rgb_image(image_rgb_data):
    image_rgb_data = image_rgb_data.astype('uint8')
    plt.imshow(image_rgb_data)
    plt.show(block=False)


def get_all_images():
    pickled_directory = "/Users/Sai/Desktop/VideoSynopsis/CSCI576ProjectMedia/Image/RGB_Pickled/"
    images = load_images(pickled_directory)
    return images


