main_number = 15
while True:
    user_input = input("Guess a number 0-20: ")
    print(f"You entered {user_input}. ")
    if int(user_input) == main_number:
        break