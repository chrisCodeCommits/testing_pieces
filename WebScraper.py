from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'



#opening the page and grabing the data
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()



#Parsing the html
page_soup = soup(page_html,'html.parser')



#Grabing each product
containers = page_soup.findAll('div',{'class':'item-container'})



#Creating a CSV file to store the data
products = 'products.csv'

f = open(products,"w")

header = 'Brand, PordactName, shipping\n'
f.write(header)


for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll('a',{'class':'item-title'})
    productName = title_container[0].text

    shipping_container = container.findAll('li',{'class':'price-ship'})
    shipping = shipping_container[0].text.strip()


    print('brand: '+ brand)
    print('productName: '+ productName)
    print('shipping: '+ shipping)

    f.write(brand+','+productName.replace(',','|')+','+shipping+'\n')

f.close()







