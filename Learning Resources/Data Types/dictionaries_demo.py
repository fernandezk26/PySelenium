#dictionaries have key value pairs
userinfo = {
    "name":"Kevin",
    "age":"28",
    "country":"USA",
    "occupation":"QA"
}

#how to extract from dictionaries
username = userinfo["name"]
print(username)

#.get a value for a key
country = userinfo.get("country")
print(country)

#key that doesn't exist will throw a key error
#city = userinfo["city"]
#print(city)

#using .get on  a key that does not exists simply states None
city = userinfo.get("city")
print(city)

#can also specify a default value
city = userinfo.get("city" , "CITY DOES NOT EXIST IN THE LIST")
print(city)

#adding item to dictionary
userinfo["city"] = "Nashville"
print(userinfo)

userinfo.update({"sex":"Male"})
print(userinfo.get("sex"))

#Trying to add a key that already exists simply overrides it
userinfo.update({"sex":"female"})
print(userinfo)

#setDefault returns the value of the item with the specified key. If Key/value pair does not exist, it adds it.
x = userinfo.setdefault("race", "Hispanic")
print(x)

x = userinfo.setdefault("sex")
print(x)

#getting all keys and all values
all_keys = userinfo.keys()
all_values = userinfo.values()

print(all_keys)
print(all_values)

# print(all_keys[0]) does not work because it is a type of Dict_Keys which is not subscriptable

#casting to a list to be able to subscript with index values
all_keys = list(userinfo.keys()) 
print(all_keys[1])

#Another example of a dictionary
employee = {
    "name":"John Doe",
    "age":25,
    "phone":4233333333,
    "title":"QA",
    "skills" : ["AWS", "QA", "Java"],
    "isActive":True
}

e_name = employee['name']
e_age = employee['age']
e_skills = employee['skills']

print(e_skills)


