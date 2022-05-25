#  #keywords in python are try and except
# try:
#     <do something>
# except <the error you want to catch, such as KeyError, Exception, IOError ,etc>  as e:
#     <do something if there is an exception>

# You can also catch multiple errors:
# except (IOError, EnvironmentError):

from ast import expr_context
from decimal import DivisionByZero


try:
    a = 5/0
except:
    print("Can't be done")

#catch a specific error
try:
    a = 5/0
except ZeroDivisionError:
    print("Don't Divide By 0")

#print the actual error
try:
    a = 5/0
except Exception as e:
    print(f"Error has happened, you did something wrong. Exception message: {e}")

#catch multiple exceptions in single block
try:
    #a = 5 / 0 
    b = {'name': 'foo', 'age': 26}
    x = b['school']

except (KeyError, ZeroDivisionError) as e:
    print(f"{e} error has happened.")
    if e == 'division by zero':
        print("Try a different number, cannot divide by 0")
    else:
        print("There is a another error, try something else")

#raising your own exception:
#raise Exception("Something went wrong")


