import requests
import sys
from urllib.parse import urlparse
from urllib.request import urlopen
import urllib.request 

def download(url,name):
    response = urllib.request.urlopen(url)    

    file = open( str(name) + ".pdf", 'wb')
    file.write(response.read())
    file.close()

def main():
    mainurl='https://jkgad.nic.in/common/showOrder.aspx?actCode=O'
    for i in range(38737,38500,-1):
        url = str(mainurl)+str(i)
        print(url)
        download(url,i)
        print("File Downloaded!")

main()
