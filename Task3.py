# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(x, y, z):
    cheat = [x, y, z]
    cheat.sort()
    return (cheat[1] + cheat[2])


user_argument1 = int(input("Введите первое значение: "))
user_argument2 = int(input("Введите второе значение: "))
user_argument3 = int(input("Введите третье значение: "))

print(my_func(user_argument1, user_argument2, user_argument3))
