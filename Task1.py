# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

division_numbers = lambda first_number, second_number: user_number1 / user_number2
user_continium = 'Y'

while user_continium.upper() == 'Y':
    user_number1 = int(input('Введите первое значение: '))
    user_number2 = int(input('Введите второе значение: '))
    try:
        print(division_numbers(user_number1, user_number2))
        user_continium = input('Q - Выход\nY - Попробовать еще раз\n: ')
    except ZeroDivisionError:
        user_continium = input('===========================\n'
                               'Вы не можете делить на ноль\n'
                               '===========================\n'
                               'Q - Выход\nY - Попробовать еще раз\n: ')
