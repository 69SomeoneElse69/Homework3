# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Реализовать вывод данных о пользователе одной строкой.
def user_profile(name, surname, bd, town, mail, phone):
    print(user_surname + " " + user_name + " (год рождения:" + str(user_bd) +
          " город:" + user_town + " email:" + user_mail + " Телефон:" + str(user_phone) + ")")


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_bd = int(input('Введите год рождения: '))
user_town = input('Введите город: ')
user_mail = input('Введите @mail: ')
user_phone = int(input('Введите телефон: '))

# Функция должна принимать параметры как именованные аргументы.
user_profile(name=user_name, surname=user_surname, bd=user_bd, town=user_town, mail=user_mail, phone=user_phone)
