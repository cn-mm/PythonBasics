import cv2
import re
import webbrowser
import requests 
import os
import shutil
from urllib.request import Request, urlopen
import bs4 as bs
import funcs

AGENT = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


query = 'synesthesia'
url = 'https://www.google.co.in/search?q='+query+'&source=lnms&tbm=isch'

# url = 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt'

res = requests.get(url)

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(type(res))
soup = bs.BeautifulSoup(res.text, 'lxml')
print(type(res.text))

'''
images = soup.select('div img')
print(len(images))  # returning only only 20 images 
print(type(images))
print(images[-1])   # prints the class and the src 
print(images[10].attrs)
for i in range(len(images)):
    print(images[i].get('src'))    # gives link to the site where the image can be found 

# print(type(soup.encode("utf-8")))

#(res.text[:200].encode("utf-8")) # gives me bytes 

'''

#making new folder and deleting prev one 
os.makedirs('new')


imgElem = soup.select('div img')     #getting img tag under  comic divison

for i in range(1,len(imgElem)):
    if imgElem == []:                        #if not found print error
        print('could not find comic image')

    else:
        try:
            print("Inside try block")
            imgUrl = imgElem[i].get('src')
            print(imgElem[i].get('src'))
            print('Downloading image %s.....' %(imgUrl))
            res = requests.get(imgUrl)
            res.raise_for_status()

            #except requests.exceptions.MissingSchema:
        except Exception as e:
        #skip if not a normal image file
            print(e)
            
        num = str(i)
        imageFile = open(os.path.join('.\\new', num),'wb')     #write  downloaded image to hard disk
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
            
        imageFile.close()


'''

res1 = Request(url, headers= AGENT)
print(type(res1))
sauce = urlopen(res1).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
print(type(sauce))  #bytes
print(type(soup))   #bs4.BeautifulSoup
'''