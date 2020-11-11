# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def user_sum(words, curent_sum):
    numbers = words.split(' ')
    if numbers.count('Q') >= 1:
        numbers.pop(numbers.index('Q'))

    for i in range(len(numbers)):
            try:
                curent_sum = int(numbers[i]) + curent_sum
            except ValueError:
                print(numbers[i], '- не является числом!')

    return (curent_sum)


main_sum = 0
user_words = []
while user_words.count('Q') < 1:
    user_words = input('Введите числа через пробел\nДля остановки используйте - Q\n: ')
    user_words = user_words.upper()
    main_sum = user_sum(user_words, main_sum)
    print(main_sum)
