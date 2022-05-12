#This is a random thing I thought of to show the while loop
user1 = {
    "password":"1234"
}

counter = 0
password = ""
lockedOut = False
authenticated = False

while password != user1["password"] and lockedOut == False:
    password = input("Enter the password: ")
    if password != user1["password"]:
        print("incorrect pasword, try again.")
        counter += 1
        if counter > 5:
            print("You are locked out buddy.")
            lockedOut = True
    else: 
        print("You have entered the correct password")
        authenticated = True

if authenticated:
    name = input("Welcome to the program, what is your name? ")
    age = input(f"Hello {name} how old are you? ")
    print(f"Cool, you are {age} years old? I'm going to sleep now, goodbye.")