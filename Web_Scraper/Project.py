import bs4 as bs
from urllib.request import Request, urlopen
import webbrowser

query = str(input("Enter your query: "))
query= query.split()
query='+'.join(query)
print(query)

path = 'https://www.google.co.in/search?q='+query+'&source=lnms&tbm=isch'
webbrowser.open(path, new = 2)


#BROWSER USER AGENT 
agent = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

req = Request(path, headers= agent)
sauce = urlopen(req).read()

soup = bs.BeautifulSoup(sauce, 'html.parser')
print(soup.encode('utf-8'))