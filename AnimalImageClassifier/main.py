# main file or the driver file

#Before running this call the webScrapper to populate the images
# WebScraper.py


import ImageProcessing
import CreateSplits
import numpy as np


if __name__ == "__main__":


    # ImageProcessing step begins
    # 1. change the directory to "/Users/Hacker_arul/MyDesktop/Masters/DeepLearningProjects/AnimalImageClassifier"
    PATH = ImageProcessing.check_dir()

    # 2. Traversing to the images folder
    ImageProcessing.change_dir(PATH=PATH+'/Images')

    # 3. Get the images directory listing
    images_dir_listing = ImageProcessing.dir_listing(PATH=PATH+'/Images/')

    # 4. Get the processed Images (lists)
    img_lst, label_lst = ImageProcessing.process_images(images_dir_listing[1:])

    # 5. create the image arrays
    X,y = ImageProcessing.create_image_arrays(img_lst,label_lst)
    print('X shape :', X.shape)
    print('y shape :', y.shape)
    print('X max num:{} , min num:{}'.format(np.amax(X),np.amin(X)))


    '''
    #testing the labels once
    print(y[0])
    print(y[283])
    print(y[581])
    print(y[889])
    print(y[1174])
    print(y[1488])
    print(y[1757])
    print(y[2072])
    '''





