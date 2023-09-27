"""
Задача 1.
    Напишите функцию, которая принимает на вход строку
    (Hello world) и возвращает ее в обратном порядке.
"""
# # Решение
def strf(str_inp):
    return str_inp[::-1]

str_inp = 'Hello world'
rev_str = strf(str_inp)
print(rev_str)





"""
Задача 2.
    Напишите функцию, которая принимает на вход список чисел 
    [10, 15, 20, 25, 50, 55, 100, 111, 122] и возвра
    щает только четные числа из этого списка.
"""
# # Решение

def get_n(in_list):
    even_n = [i for i in in_list if i%2==0]
    return even_n
in_list=[10, 15, 20, 25, 50, 55, 100, 111, 122]
evenn = get_n(in_list)
print(evenn)





"""
Задача 3.
                                       Угадай число
    Бот с помошью модуля random загадывает число в диапазоне от 1 до 30.
    Напишите программу которая будет спрашивать у пользователя число(загаданное ботом) и будет
    выводить:

    Загаданное число меньше. - если число которое загадал бот меньше введенного числа пользователем
    Загаданное число больше. - если число которое загадал бот больше введенного числа пользователем
    Вы угодали! - если введенное число совпадет с загаданным числом

    Программа должна считать количество попыток от пользователя. 
    (Сколько ходов потребовалось пользователю чтобы угадать число)
В конце должен спрашивать у пользователя "Желаете поиграть снова?(y/n)
      " - в случае если пользователь выберет "y" то пусть бот загадает новое число
        и игра начнется сначала.
В случае если пользователь введет "n" - пусть выведется текст "Спасибо за игру!" и программа завершится.
"""
# # Решение

import random


def guess_n_game():
    b = random.randint(1,30)
    k = 0
    
    
    while True:
        user_guess = int(input('Enter number: '+'\n'))
        k += 1
        
        
        if user_guess < b:
            print('<')
        elif user_guess > b:
            print('>')
        else:
            print(f'ugadali chislo kolichestvo popitki {k}')
            play_again = input('Play again ("y/n"):'+'\n')
            if play_again.lower() != "y":
                print('Thank you ')
                break
            
guess_n_game()




"""
Задача 4.
    Напишите функцию, которая принимает на вход неопределенное количество чисел и возвращает их сумму.
"""
# # Решение


def power_numbers(**kwargs):
    powered_numbers = [value ** kwargs['power'] for value in kwargs.values()]
    return powered_numbers


result = power_numbers(num1=2, num2=3, num3=4, power=2)
print(result) 




"""
Задача 5.
     Напишите функцию, которая принимает на вход неопределенное количество ключевых аргументов 
     (число и степень) и возвращает список чисел, возведенных в указанную степень.
"""
# # Решение
# 1)

def powern(*args):
    p = [num ** po for num, po in args]
    return p

res = powern((2, 1), (3, 2), (5, 3), (2, 4))
print(res)



#2)

def poswe(**kv)->int:
    lis = [v ** kv['v'] for v in kv.values()]
    return lis

r = poswe(v=2,v3=3)
print(r)




"""
Задача 6.
    Напишите функцию, которая принимает на вход список чисел [1, 2, 3, 4, 5, 6, 7, 8]
    и необязательный аргумент "reverse" (по умолчанию False).
    Если аргумент reverse равен True, 
    то функция должна вернуть список чисел в обратном порядке, иначе - в исходном порядке.
"""
# Решение


def rev_l(num, reverse=False):
    if reverse:
        return list(reversed(num))
    else:
        return num


list_ = [1, 2, 3, 4, 5, 6, 7, 8]
result = rev_l(list_)
print(result)  

r_rev = rev_l(list_, reverse=True)
print(r_rev)  




"""
Задача 7.
    Напишите код с помощью модулья, где показывает текущую дату и время.
"""
# # Решение

import datetime


time = datetime.datetime.now()
print(time)





"""
Задача 8.
    Напишите функцию del(a, b), которая будет делить число a на число b. 
    Функция должна возвращать результат деления.
     Если происходит деление на ноль, функция должна выводить сообщение "Деление на ноль невозможно"
      и возвращать None.
"""
# # Решение

def kal():
    a = float(input('Enter number: '))
    b = float(input('Enter number: '))
    
    
    if a == 0:
        print('chislo a ravno nuly, delenie na nol nevozmojno')
        return None
    elif b == 0:
        print('Delenie na nol nevozmojno')
        return None
    else:
        return a / b

res = kal()
if res is not None:
    print(f'Resultat delenie: {res}')


    




"""
Задача 9.
    Создайте функцию anotations(...) которая принимает 5 аргументов и их параметры (умножте все параметры)
     и  создайте анотацию для этой функции
"""
# Решение


from typing import Any


def anno(ar1:Any,ar2:Any,ar3:Any,ar4:Any,ar5:Any)->Any:
    res = ar1 * ar2 * ar3 * ar4 * ar5
    return res

res = anno(2,3,4,5,6)
print(res)







"""
Задача 10.
    Напишите функцию json(file_name, key, value),
    которая будет обновлять значение по ключу key в JSON файле с именем file_name на значение value.
     Если происходит ошибка при обновлении файла, функция должна выводить сообщение 
     "Ошибка обновления файла".
"""
# # Решение

def jsu_json(fil,k,v):
    try:
        with open(fil,'r') as f:
            data = json.load(f)
            
        data[k] = y
        
        with open(fil,'w') as f:
            json.dump(data,f,index=2)
            
    except Exception as e:
        print("Oshibka ", str(e))
        
        
fil = 'data.json'
k = 'k.key'
v = 'v.value'
jsu_json(fil,k,v)



import time

def lis():
    list_ = []
    for i in range(1,51):
        list_.append(i)
    return list_

def liscom():
    listcom_=[i for i in range(1,51)]
    return listcom_


starlist = time.time()
lis()
endlist = time.time()
reslist = endlist - starlist

startcomlist = time.time()
liscom()
endlistcom = time.time()
resliscom = endlistcom - startcomlist

print(f'{endlist}')
print(f'{resliscom}')