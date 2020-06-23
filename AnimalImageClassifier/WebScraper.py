#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:12:53 2020

@author: Hacker_arul
"""

import requests
from bs4 import BeautifulSoup
import os


def get_urls(url_head,animals):
    #defining the lists to store the urls
    urls_tiger = []
    urls_deer = []
    urls_elephant = []
    urls_horse = []
    urls_lion = []
    urls_snake = []
    urls_zebra = []
    urls_giraffe = []
    
    for i in range(len(animals)):
        if i == 0:
            for page in range(6):
                urls_deer.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 1:
            for page in range(6):
                urls_elephant.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 2:
            for page in range(6):
                urls_giraffe.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 3:
            for page in range(6):
                urls_horse.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 4:
            for page in range(6):
                urls_lion.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 5:
            for page in range(6):
                urls_snake.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i ==6:
            for page in range(6):
                urls_tiger.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        elif i == 7:
            for page in range(6):
                urls_zebra.append(url_head+animals[i]+'?mediatype=photography&phrase='+animals[i]+'&sort=mostpopular'+'&page='+str(page+1))
        else:
            print('sorry cant process the request right now!!')
   
    return urls_deer,urls_elephant,urls_giraffe,urls_horse,urls_lion,urls_snake,urls_tiger,urls_zebra

# need to process each link stored in lists 
# will go one by one for each list
def webScrapeImages(url_list,animal_name):
    counter = 0
    for url in url_list:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = []
        for link in soup.find_all("img",{"class":"gallery-asset__thumb gallery-mosaic-asset__thumb"}):
            links.append(link.get('src'))
        for index,img_link in enumerate(links):
            if index <= len(links):
                img_data = requests.get(img_link).content
                with open("Images/"+animal_name+'_'+str(counter+1)+'.jpg','wb+') as f:
                    f.write(img_data)
                    counter += 1
            else:
                f.close()
                break
    return None

if __name__ == "__main__":
    
    # get the current working directory
    # it has to be the project folder - 
    # "/Users/Hacker_arul/MyDesktop/Masters/DeepLearningProjects/AnimalImageClassifier"
    print(os.getcwd())
    # need to make the directory to save the images
    os.mkdir('Images')

    #preparing the URLs

    #creating the different urls to populate 300 different images for tiger
    url_head = "https://www.gettyimages.com/photos/"

    # the different animals we want to collect the images for
    animals = ['deer','elephant','giraffe','horse','lion','snake','tiger','zebra']
    
    urls_deer,urls_elephant,urls_giraffe,urls_horse,urls_lion,urls_snake,urls_tiger,urls_zebra = get_urls(url_head,animals)
    
    #now let's begin the scrapping of images....
    
    webScrapeImages(urls_deer,'deer')
    webScrapeImages(urls_elephant,'elephant')
    webScrapeImages(urls_giraffe,'giraffe')
    webScrapeImages(urls_horse,'horse')
    webScrapeImages(urls_lion,'lion')
    webScrapeImages(urls_snake,'snake')
    webScrapeImages(urls_tiger,'tiger')
    webScrapeImages(urls_zebra,'zebra')
    
    print("YIPEEEE!!!!!! all done, we have the images now!!!")
