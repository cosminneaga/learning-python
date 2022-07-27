import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "cos@mail.com"
wrong_email = "cos"

a = pattern.match(email)
print(a)
b = pattern.match(wrong_email)
print(b)
