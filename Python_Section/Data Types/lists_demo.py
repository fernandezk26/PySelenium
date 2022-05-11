#creating a list
users = ["Kevin","Christian","Joe"]

#printing a specific user based on index
user = users[0]
print(user)

#remove the last element
user2 = users.pop()
print(user2)

#append to the end
users.append("John")
print(user)

#splicing a list based on index
last_two = users[1:]
print(last_two)

#printing the length
print(len(users))

#removing a specific item
users = users.remove("Kevin")
print(users)