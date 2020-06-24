# MODULES 
import bs4 as bs
from urllib.request import Request, urlopen
import webbrowser
import sys
import os
import re
import requests
import cv2
import funcs # helper functions 


#BROWSER USER AGENT 
AGENT = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

EXTENSIONS = ['jpg', 'png']
NUM_IMAGES = 100

# GETTING QUERY FROM COMMAND LINE OR THE USER
def get_query():
    if len(sys.argv) > 1:
        # Get address from command line.
        query = ' '.join(sys.argv[1:])
    else:
        #Get query from user 
        option = input("Type 1 to input query ")
        if option == '1':
            query = str(input("Enter your query: "))
            print("Searching Google Images for", query)
            query= query.split()
            query='+'.join(query)
        else:
            # Use default query 
            query = "drums"
            print("Using default query \" Drums\"")

    return query


def get_url(query):
    return 'https://www.google.co.in/search?q='+query+'&source=lnms&tbm=isch'



# DIRECTORY FOR SAVING THE IMAGES 
query = get_query()
dirname = 'Scraped ' + re.sub('[!!@#$+]', ' ',query)
os.makedirs(dirname, exist_ok=True)  


try:
    res = requests.get(get_url(query))
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    # print(len(res.text))
    # print(res.text[:200])
    soup = bs.BeautifulSoup(res.text, 'html.parser')

except requests.exceptions.ConnectionError:
    res.status_code = "Connection refused"


imgElem = soup.select('div img')     #getting img tag 

for i in range(1,len(imgElem)):
    if imgElem == []:                        #if not found print error
        print('could not find any image')

    else:
        try:
            imgUrl = imgElem[i].get('src')
            print(imgElem[i].get('src'))
            print('Downloading image %s.....' %(imgUrl))
            res = requests.get(imgUrl)
            res.raise_for_status()

            #except requests.exceptions.MissingSchema:
        except Exception as e:
        #skip if not a normal image file
            print(e)
            
        num = str(i) + ".jpg"
        imageFile = open(os.path.join('.\\'+ dirname, num),'wb')     #write  downloaded image to hard disk
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
            
        imageFile.close()


'''

def main():



if __name__ == '__main__':
    main()


'''
