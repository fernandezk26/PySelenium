# create a file with a list of randomly generated email addresses. The email addresses must have a domain name from the list of domains
# domain list is provided as a list_of_domains
#create 100 total emails with domains randomly selected from the list. The numbers of each domain will be unknown

import random
import string

list_of_domains = ['gmail.com', 'outlook.com', 'yahoo.com', 'msn.com']

length_of_email = 10
letters = string.ascii_lowercase

list_of_email_addresses = []
for i in range(100):
    random_domain = random.choice(list_of_domains)
    random_string = ''.join(random.choice(letters) for i in range(length_of_email))
    email = f"{random_string}@{random_domain}"
    list_of_email_addresses.append(email)

print(list_of_email_addresses)

with open('./sample_files/out_generate-random_email_with_list_of_domains_v2.csv' , 'w') as f:
    str_list_of_domains = ',\n'.join(list_of_email_addresses)
    f.write(str_list_of_domains)