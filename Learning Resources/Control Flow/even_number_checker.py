
continue_calc = 'Y'

while continue_calc == 'Y':

    number = int(input("What is the number you want to check? "))

    if number % 2 > 0:
        print("This is an odd number")
    else:
        print("This is an even number")
    
    continue_calc = input("Would you like to check another number? Y or N ")

