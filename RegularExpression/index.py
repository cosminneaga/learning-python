import re

pattern = re.compile('this')
string = 'search this inside of this text please!'
p_full = re.compile(string)

print('search' in string)


a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())


b = pattern.search(string)
c = pattern.findall(string)
d = p_full.fullmatch(string)
e = p_full.match(string)
print(b.group())
print(c)
print(d.group())
print(e.group())
