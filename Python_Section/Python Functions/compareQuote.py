import itertools
  
# initializing list 
quote1 = [
    {"partNumber": 1792, "price": 19.99},
    {"partNumber": 1827, "price": 29.99},
    {"partNumber": 938, "price": 99.99},
    {"partNumber": 1111, "price": 929.99},
    {"partNumber": 2322, "price": 99.99}
]

quote2 = [
    {"partNumber": 1792, "price": 19.99},
    {"partNumber": 1827, "price": 28.99},
    {"partNumber": 938, "price": 99.99},
    {"partNumber": 1111, "price": 928.99},
    {"partNumber": 2222, "price": 99.99}
]

# using itertools.filterfalse()
# set difference in dictionary list 
res = list(itertools.filterfalse(lambda i: i in quote1, quote1)) \
    + list(itertools.filterfalse(lambda j: j in quote2, quote1))
  
# printing result 
print ("These items in the quote do not match : " +  str(res))