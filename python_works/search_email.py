import re


def extract_emails():
    with open('textfile.txt', 'r') as file:
        data = file.read()

    email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
    unique_email_list = list(set(email_list))

    return unique_email_list

print(extract_emails())