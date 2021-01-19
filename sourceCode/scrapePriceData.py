from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.nkon.nl/lg-inr18650-mj1.html')
bsObj = BeautifulSoup(html)
requiredContainer = bsObj.find("div", {'class':'price'})

holdValue = requiredContainer.find("div", {'class':'price'})
print(holdValue)

sevenValue = requiredContainer.find('div', {'class':'value'})
print(sevenValue)