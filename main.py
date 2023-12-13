first_digit = int(input())
second_digit = int(input())
math = input()

if second_digit == 0 and math == '/':
    print('На ноль делить нельзя!')
elif math == '/':
    print(first_digit / second_digit)
elif math == '*':
    print(first_digit * second_digit)
elif math == '+':
    print(first_digit + second_digit)
elif math == '-':
    print(first_digit - second_digit)
else:
    print('Неверная операция')



