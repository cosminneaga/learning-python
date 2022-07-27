import re

# pattern = re.compile('"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"')
pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search this inside of this text please! Cosmin'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group())
print(a.group(1))
print(a.group(2))
