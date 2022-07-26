# by = input('Your year of birth\n')
# age = 2022 - int(by)
# print(f'Your age is around {age} yo')

user = input('Enter user:\n')
password = input('Enter password:\n')
password_length = len(password)
hidden_password = '*' * password_length

print(f'{user} your password {hidden_password} is {password_length} letters long')
