# #example 1
# main_number = 15
# while True:
#     user_input = input("Guess a number 0 to 20: ")
#     print(f"You entered: {user_input}.")
#     if int(user_input) == main_number:
#         break
#     else:
#         continue

# print("Done!")

# #example 2
# user1 = {
#     "password":"1234"
# }

# counter = 0
# password = ""
# authenticated = False

# while password != user1["password"] and authenticated == False:
#     password = input("Enter the password: ")
#     if password != user1["password"]:
#         print("incorrect pasword, try again.")
#         counter += 1
#         if counter > 5:
#             print("You are locked out buddy.")
#             break
#     else: 
#         print("You have entered the correct password")
#         authenticated = True

# if authenticated: 
#     name = input("Welcome to the program, what is your name? ")
#     age = input(f"Hello {name} how old are you? ")
#     print(f"Cool, you are {age} years old? I'm going to sleep now, goodbye.")


#problem: given a country, print the capital city if it is in the set of data, else print capital not found

capitals = {
    "Peru":"Lima",
    "Phillipines":"Manila",
    "Spain":"Madrid",
    "Ethiopia":"Addis Ababa",
    "Ghana":"Accra"
}


# user_input = input("Enter a country: ")
# for country in list(capitals):
#     if user_input == country:
#         capital = capitals[user_input]
#         break
#     else:
#         capital = "Capital Not Found"

# print(capital)

#example 3: given a dictionary with book prices and a list of courses, calculate the total cost of books
book_prices = {"calculus": 300, "physics":500, "math": 300, "biology":150}
my_courses = ["calculus", "physics", "history"]
total_cost = 0

for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]

print(f"The total cost is {total_cost}")
