# MODULES 
import bs4 as bs
from urllib.request import Request, urlopen
import webbrowser
import sys
import os
import json
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




query = get_query()
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

# DIRECTORY FOR SAVING THE IMAGES 
os.makedirs('Scraped ' + re.sub('[!!@#$+]', ' ',query), exist_ok=True)  




image_elements = soup.find('img')
print(type(image_elements))
print(image_elements)



'''
metadata_dicts = (json.loads(e.text) for e in image_elements)
link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)

print(link_type_records)


def main():



if __name__ == '__main__':
    main()


'''
