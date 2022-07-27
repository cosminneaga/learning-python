import re

# min 8 char long
# contain any sort letters, numbers, $%#@


pattern = re.compile(r"[a-zA-z0-9#@%$]{8,}\d")

pass1 = "absGfs@s$#@323"
pass2 = "absGfs@dasd"

a = pattern.match(pass1)
print(a)
b = pattern.match(pass2)
print(b)
