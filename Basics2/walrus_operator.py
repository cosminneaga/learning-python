# :=

a = 'heeeeeeeeeelllloooo'

if len(a) > 10:
    print(f'too long {len(a)} elements')

print()
if (n := len(a)) > 10:
    print(f'too long {n} elements')


print()
while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
