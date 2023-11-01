# Программа загадывает число и просит угадать его
# Если веденное числ больше, то просит ввести меньшее число и наоборот и так до конца
import random
def start(): # начало и границы
    print('Добро пожаловать в числовую угадайку')
    print('Укажите границы чисел через Enter')
    x, y = int(input()), int(input())
    if x > y:
        x, y = y, x
    print('Отлично!! Начнем игру')
    examin(x, y)

def is_valid(x, y): # проверка числа
    while True:
        num = input()
        if num.isdigit() == False or (x > int(num) or int(num) > y):
            print('А может быть все-таки введем целое число в заданном вами диапозне?')
        else:
            num = int(num)
            return num
            break
def examin(x, y): # угадайка
    print('введите число в заданном вами диапозоне:')
    rand_num = random.randint(x, y)
    s = 0
    while True:
        num = is_valid(x, y)
        if num > rand_num:
            print('Слишком много, попробуйте еще раз')
            s += 1
        elif num < rand_num:
            print('Слишком мало, попробуйте еще раз')
            s += 1
        else:
            if s == 0:
                print('Количесто попыток:', s)
                print('Да ты красава. Я так точно не смогу')
                break
            else:
                print('Вы угадали, поздравляем!')
                print('Количесто попыток:', s)
                break
    repeat()

def repeat(): # повтор
    print('хотите сыграть еще раз?', '1(да)/0(нет)')
    while True:
        n = input().lower()
        if n == 'да' or n == '1':
            start()
            break
        elif n == 'нет' or n == '0':
            print('Удачи! Увидимся в следующий раз')
            break
        else:
            print('Я не понимаю вашего ответа, попробуйте снова')
start()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')