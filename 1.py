# Это однострочный комментарий
"""
Это многострочный комментарий
"""
x = 5          # Integer (целое число)
y = 3.14       # Float (дробное число)
""" name = "Алиса" # String (строка)
name = 'Алиса' # String (строка)
is_active = True # Boolean (булевая переменная)
user_name = input("Введите имя: ")
surname = input("Введите фамилию: ")
print("Привет,", user_name, surname, "!") """
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

age = 30
print("Name: {}, Age: {}".format(full_name , full_name, age))
contract_template = " This is a SAMPLE contract for the CLIENT. "

# Removing leading and trailing spaces
contract_template = contract_template.strip()

# Converting to uppercase
print(contract_template.upper()) # Output: THIS IS A SAMPLE CONTRACT FOR THE CLIENT.

# Converting to lowercase
print(contract_template.lower()) # Output: this is a sample contract for the client.

# Title case
print(contract_template.title()) # Output: This Is A Sample Contract For The Client.

# Replacing words
contract_template = contract_template.replace("CLIENT", "John Doe")
print(contract_template) # Output: This is a SAMPLE contract for the John Doe.

# Splitting and joining
words = contract_template.split()
print(words) # Output: ['This', 'is', 'a', 'SAMPLE', 'contract', 'for', 'the', 'John', 'Doe.']
updated_contract = " ".join(words)
print(updated_contract) # Output: This is a SAMPLE contract for the John Doe.
print (contract_template.split("contract"))

template = """
This CONTRACT is made on {date} between {party1} and {party2}.

WHEREAS, {party1} agrees to provide the following services: {services}.

NOW, THEREFORE, the parties agree as follows:

1. TERM: The term of this contract shall commence on {start_date} and terminate on {end_date}.
2. PAYMENT: {party1} shall be compensated as follows: {payment_terms}.

IN WITNESS WHEREOF, the parties have executed this contract as of the date first written above.
"""
# Taking input from the user
date = input("Enter the date: ")
party1 = input("Enter the first party: ")
party2 = input("Enter the second party: ")
services = input("Describe the services: ")
start_date = input("Enter the start date: ")
end_date = input("Enter the end date: ")
payment_terms = input("Describe the payment terms: ")

# Filling the template
contract = template.format(date=date, party1=party1, party2=party2, services=services, start_date=start_date, end_date=end_date, payment_terms=payment_terms)
print(contract)
