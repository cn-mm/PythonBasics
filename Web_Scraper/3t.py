# Resources:
# https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

print("run imports...")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import argparse
import urllib.request
import requests
import sys
import re
from helper_funcs import get_url, get_query


# SEARCH INFO 
print("Enter query for downloading Google Images...")
searchterm = get_query() # will also be the name of the folder
url = get_url(searchterm)

# NUMBER OF IMAGES 
num = int(input("Enter number of images required: "))

# MAKE DIRECTORY FOR STORING IMAGES 
dirname = 'Scraped ' + re.sub('[!!@#$+]', '_',searchterm) + '_' + str(num)
os.makedirs(dirname, exist_ok=True)  

# SELENIUM WEBDRIVER 
browser = webdriver.Chrome(executable_path=r'C:/Users/Hp/Downloads/chromedriver.exe')
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0


print("Scrolling to generate images...")
# Keep scrolling down by 10000 until required number of images downloaded 
try:
    while(succounter <= num) : 
        browser.execute_script("window.scrollBy(0,100)")    
        print("Let the scraping begin:")
        for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
            counter += 1
            print("Total Count:", counter)
            print("Succsessful Count:", succounter)
            print("URL:", x.get_attribute('src'))

            img = x.get_attribute('src')
            new_filename = "image"+str(counter)+".jpg"

            try:
                path = 'C:/Users/Hp/Desktop/Wobot/VS/'+dirname+ '/'
                path += new_filename
                urllib.request.urlretrieve(img, path)
                succounter += 1
            except Exception as e:
                print(e)

        print(succounter, "Pictures successfully downloaded")
        browser.quit()
                
        
    else:
        print("{} Images found for the query {}".format(num, searchterm))
except Exception as e:
    print("There was an error %s" %e)


