# This is our main.
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url  = 'https://www.newegg.com/p/pl?d=graphics+cards'

#Opening up connection and grabbing the page
uClient = uReq(my_url)
#Save it to a vairable cause it's a simple html file to prevent crashing
page_html = uClient.read()
#close the website you scraped
uClient.close()
# Html passing
page_soup = soup(page_html, "html.parser")
# grabs each product. Even though this is for graphics cards, you can parse different parts of the website
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name\n"
f.write(headers)
for container in containers:
	#Grabbing using their div tag the brand name, the title of the product and the specific na,e
	brand = container.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	# shipping container returned an empty array
	# shipping_container = container.findAll("li", {"class":"price-ship"})
	#shipping =  shipping_container[0].text.strip()
	print("brand: " + brand)
	# print("title_container: " + title_container)
	print("product_name: " + product_name)

	f.write(brand + "," +product_name.replace(",", "|")+ "\n")
f.close()