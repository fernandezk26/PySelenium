# isActive = True
# while isActive == True:
#     action = input("Would you like to terminate the user? 'Y' or 'N' ")
#     if action == 'Y':
#         isActive = False
#         print("The User has been TERMINATED")
#     else: 
#         isActive = True
#         print("The User is still active")

# counter = 1
# while counter < 20:
#     print(counter)
#     counter += 1

password = ""
while password != "1234":
    password = input("Enter the password: ")
    if password != "1234":
        print("incorrect pasword, try again.")
    else: 
        print("You have entered the correct password")