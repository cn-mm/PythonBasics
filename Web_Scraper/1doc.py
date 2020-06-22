html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml') # can use any parser, (lxml, html.parser, html5lib)

# print(soup.prettify()) #TYPE IS STR TYPE 

#-------------------------------------------------------------------------------------------------------------

# Access html files in the directory
with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.prettify())

#TAGS 
soup = BeautifulSoup("<html>a web page</html>", 'lxml')
# tag = soup.html
# tag = soup.p
tag = soup.string
print(tag, type(tag))

#Cannot edit string but it can be replaced with another string using replace_with()

#-------------------------------------------------------------------------------------------------------------

def writeToFile(soup):
    #WRITING TO A FILE 
    textFile = open('Pretty alice.txt', 'w')
    textFile.write(soup.prettify())

    textFile.close()

#-------------------------------------------------------------------------------------------------------------
def printTitle(soup):
    # NAVIGATING THE DATA STRUCTURE

    #TITLE:
    print(soup.title)
    # <title>The Dormouse's story</title>

    print(soup.title.name)
    # u'title'

    print(soup.title.string)
    # u'The Dormouse's story'

    print(soup.title.parent.name)
    # u'head'

def printParagraphs(soup):
    #PARAGRAPHS 
    print(soup.p)
    # <p class="title"><b>The Dormouse's story</b></p>

    print(soup.p['class'])
    # u'title'

def printLinks(soup):
    # Extracting all the URLs found within a page’s <a> tags
    print(soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    print(soup.find_all('a'))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(soup.find(id="link3"))
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    for link in soup.find_all('a'):
        print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

def printText(soup):
    #EXTRACTING ALL TEXT FROM THE WEBPAGE 
    print(soup.get_text())
    # The Dormouse's story
    #
    # The Dormouse's story
    #

#-------------------------------------------------------------------------------------------------------------