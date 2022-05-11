#lets say I want to verify a URL is at the home page when I click a link
url = "https://www.google.com/home"
is_home = url.endswith(".com/home")
if is_home == True:
    print("The button took me to the correct home page")
else:
    print("This did not take you to the home page")

#splitting string to list
fullname = "Kevin Fernandez"
user_info = fullname.split()
print(user_info)

#splitting based on specific characters, like if I want to strip away dashes from a SSN
ssn = "555-555-1111"

#remove the slashes, enter into list
ssn = ssn.split('-')

#display only the last 4
print("the last for of the SSN are:" + " " + ssn[-1])

#using fstring for the same thing
print(f"the last four of the SSN are {ssn[-1]}")


#strip to remove white spaces at the beginning or the end of a string
fname = "     kevin fernandez         "
print(fname)
fname_clean = fname.strip()
print(fname_clean)

#.replace can remove white spaces or anything else within a string
state = "F lorida"
print(state)
state = state .replace(' ','')
print(state)
