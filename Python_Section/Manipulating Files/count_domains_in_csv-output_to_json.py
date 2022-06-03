import json
#read the list of email addresses fromt eh input file and create a dictionary with keys being domain name
#and value keys being the number of occurences for the domain. Save the output as a .json file

#input file: count_domains_in_email_list_file_exercies_input.csv
#output file: count_domains_in_email_list_file_exercise_output.json

def read_emails_list(file_path): 
    #read the email and format into a list
    with open(file_path , 'r') as f:
        emails_list = f.read()
        emails_list = emails_list.split(',\n')

    #iterate through the list and remove everything after the @
    domain_list = []
    for email in emails_list:
        domain = email.split('@')[1]
        domain_list.append(domain)

    return domain_list
# print(domain_list)
domain_list = read_emails_list('./sample_files/out_generate-random_email_with_list_of_domains_v2.csv')

def count_unique_domains(domain_list):
#find each unique domain and add to a dictionary with no value
    counter = 0
    unique_domains = {}
    for domain in domain_list:
        if domain not in unique_domains:
            unique_domains[domain] = 1
        else:
            unique_domains[domain] = unique_domains[domain] + 1

    return(unique_domains)

    # #The easy way
    # from collections import Counter
    # count_dict = dict(Counter(domain_list).items())

unique_domains = count_unique_domains(domain_list)

print(unique_domains)

def save_output_to_json(unique_domains, json_file_path):
    with open(json_file_path , 'w') as f:
        #dumps turns dict into json
        json_object = json.dumps(unique_domains)
        f.write(json_object)

save_output_to_json(unique_domains=unique_domains, json_file_path='./sample_files/count_domains_in_email_list_file_exercise_output.json')

