products = [
    {"id" : 1, "price" : 12.99, "desc" : "Brown Ugly Shirt", "is_on_sale" : True, "sale_price": 0, "qty" : 10},
    {"id" : 2, "price" : 25.99, "desc" : "Grandmas Underwear", "is_on_sale" : False, "sale_price": 0, "qty" : 10},
    {"id" : 3, "price" : 1.99, "desc" : "Singular Dirty Sock", "is_on_sale" : False, "sale_price": 0, "qty" : 10},
    {"id" : 4, "price" : 18.99, "desc" : "Sweater", "is_on_sale" : True, "sale_price": 0, "qty" : 10},
    {"id" : 5, "price" : 199.99, "desc" : "Cashmere shirt", "is_on_sale" : True, "sale_price": None, "qty" : 10}
]

print("exercise 1: Iterate through all of the items and print the ones that have a price higher than $25 \n")
for product in products:
    if product["price"] >= 25:
        print(product["desc"], product["price"])

print("___________________________________________________________________________________________________________________________\n")
print("exercise 2: Iterate through all of the items and print the ones that are on sale\n")
for product in products:
    if product["is_on_sale"] == True:
        print(product["desc"], product["sale_price"])

print("___________________________________________________________________________________________________________________________\n")
print("exercise 3: iterate through all of the items and print any items that are on sale but do not have a sale price")
for product in products:
    if product["is_on_sale"] == True:
        if product["sale_price"] == None:
            print(product["desc"] + " is on sale but does not have a sale price assigned. ")