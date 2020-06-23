#ImageProcessing.py
# Processes the images - resize, converting to numpy arrays etc.

import os
import numpy as np
import cv2

def check_dir():
    # checking the directory path
    # has to be "/Users/Hacker_arul/MyDesktop/Masters/DeepLearningProjects/AnimalImageClassifier"
    if os.getcwd() != "/Users/Hacker_arul/MyDesktop/Masters/DeepLearningProjects/AnimalImageClassifier":
        os.chdir("/Users/Hacker_arul/MyDesktop/Masters/DeepLearningProjects/AnimalImageClassifier")
        print("Directory changed")
    PATH = os.getcwd()
    print('PATH :', PATH)
    return PATH

def change_dir(PATH):
    os.chdir(PATH)
    return None

def dir_listing(PATH):
    return sorted(os.listdir(PATH), reverse=False)

def process_images(images_dir_listing):

    labels = {'deer':0, 'elephant':1, 'giraffe':2, 'horse':3, 'lion':4, 'snake':5, 'tiger':6, 'zebra':7}
    #attributes for image processing
    num_rows_image = 200
    num_cols_image = 200
    label = -1
    #lists to be populated
    img_data_list = []
    class_labels = []

    for image in images_dir_listing:
        if 'deer' in image:
            label = labels['deer']
        elif 'elephant' in image:
            label = labels['elephant']
        elif 'giraffe' in image:
            label = labels['giraffe']
        elif 'horse' in image:
            label = labels['horse']
        elif 'lion' in image:
            label = labels['lion']
        elif 'snake' in image:
            label = labels['snake']
        elif 'tiger' in image:
            label = labels['tiger']
        elif 'zebra' in image:
            label = labels['zebra']
        else:
            print('sorry cant process the request made!!')
        img = cv2.resize(cv2.imread(image), (num_rows_image, num_cols_image))
        img_data_list.append(img)
        class_labels.append(label)

    return img_data_list,class_labels

def create_image_arrays(img_list,label_list):
    num_samples = len(img_list)
    #creating the array from the image list
    X = np.array(img_list)
    y = np.array(label_list)
    X = X.astype('float32')
    X = X / 255.0 - 0.5      #scaling the data between 0 and 1
    assert X.shape[0] == num_samples
    return X,y



