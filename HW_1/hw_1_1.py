# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
year = int(input('Введите ваш год рождения: '))
country = input('Ваша страна проживания: ')
city = input('Введите ваш город проживания: ')

user_info = (
    f" Ваше имя: {name}, возраст: {age}, год рождения: {year}, город проживания: {city}, страна проживания: {country}")

print(user_info)