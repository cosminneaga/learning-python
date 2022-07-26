
def sum(n1, n2):
    try:
        return n1 / n2
    except (TypeError, ZeroDivisionError) as e:
        return f'please enter numbers only - {e}'


print(sum('1', 2))
print(sum(1, 0))


while True:
    try:
        age = int(input('what is your age? '))
        print(age)
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break
    finally:
        print('ok, I\'m finally done!')
