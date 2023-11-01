# Программа запрашивает количество поролей и ее длину, а также все необходимые данные для создание пороля
# На всех необходимый данных программа пишет различные и безопасные пороли и выводит их
import random
def check_of(a):
    pos_answer = ['да', 'конечно', 'yes', '1']
    nog_answer = ['не надо', 'no', 'нет', '0']
    n = input().lower()
    while True:
        if n in pos_answer:
            return 'да'
            break
        elif n in nog_answer:
            return 'нет'
            break
        else:
            print('Я вас не понимаю, попробуйте по другому')
            n = input().lower()
print('Добро пожаловать в "Генератор безопасных паролей".')
print('Эта программа создана специально, чтобы помочь вам создать безопасный пороль.')
print('Давайте начнем!')
quantity = int(input('Какое количество паролей для генерации вы хотите? - '))
len_wassword = int(input('Какую длину пароля вы хотите? - '))
num = check_of(print('Включать ли цифры 0123456789?'))
upper = check_of(print('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?'))
lower = check_of(print('Включать ли прописные буквы abcdefghijklmnopqrstuvwxyz?'))
symbol = check_of(print('Включать ли символы !#$%&*+-=?@^_?'))
amb_char = check_of(print('Исключать ли неоднозначные символы il1Lo0O?'))
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=@^_.'

for i in range(quantity):
    char = ''
    while True:
        if num == 'да':
            char += random.choice(digits)
            if len(char) == len_wassword:
                break
        if upper == 'да':
            char += random.choice(uppercase_letters)
            if len(char) == len_wassword:
                break
        if lower == 'да':
            char += random.choice(lowercase_letters)
            if len(char) == len_wassword:
                break
        if amb_char == 'нет':
            char += random.choice('il1Lo0O')
            char += random.choice(lowercase_letters)
            if len(char) == len_wassword:
                break
    print(char)
print('Спасибо, что пользовались нашими услугами.')
print('До новых встреч!!!')