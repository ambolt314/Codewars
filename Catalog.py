from bs4 import BeautifulSoup

def catalog(s, article):
    soup = BeautifulSoup(s, "html.parser")
    products = soup.find_all('prod')
    
    catalog = []
    
    for product in products:
        name = product.find('name').text
        price = product.find('prx').text
        quantity = product.find('qty').text
        catalog.append(Product(name, price, quantity))
    
    catalog = list(filter(lambda p: article in p.name, catalog))
    
    if len(catalog) == 0:
        return "Nothing"
    
    output = ""
    for i in range(len(catalog)):
        output += "{} > prx: ${} qty: {}".format(catalog[i].name, catalog[i].price, catalog[i].quantity)
        if i != len(catalog) - 1:
            output += "\r\n"
        
    return output
        
    
class Product:
    name = ""
    price = ""
    quantity = ""
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
