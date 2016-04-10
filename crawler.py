import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.sastra.edu')
source = response.text
soup = BeautifulSoup(source)
for atag in soup.findAll("a"):
    if (atag.get("href").startswith("http://")):
        print (atag.get("href"))
        new_link = requests.get(atag.get("href"))
        new_source = new_link.text
        soup1 = BeautifulSoup(new_source)
        for meta in soup1.findAll("meta",{"name":"description"}):
            print (meta.get("content"))