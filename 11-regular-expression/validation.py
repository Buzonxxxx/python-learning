import re

def validate_email(email):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return pattern.search(email)

def validate_password(password):
    pattern = re.compile(r"^[a-zA-Z0-9%$#@]{8,}\d$")
    return pattern.match(password)

# Testing email validation
email = 'example@example.com'
if validate_email(email):
    print(f"{email} is a valid email.")
else:
    print(f"{email} is not a valid email.")

# Testing password validation
password = 'dsajfsadkjgak437598$%$$#8'
if validate_password(password):
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")