# Шифр Цезаря
# На входе, программе подается действие зашифровки или расшифровки текста
# После чего запршиваеться язык и текст, который будет использоваться для дальнешего превращения
def english():
    b = ''
    a = input('Введите тест - ')
    n = int(input('Какой сдвиг? - '))
    for i in a:
        k = int(ord(i))
        if 97 <= k <= 122:
            i = chr(k+n)
            if k+n > 122:
                i = chr((k+n - 122) + 96)
        b += i
    return print(b)
def russian():
    b = ''
    a = input('Введите тест - ')
    n = int(input('Какой сдвиг? - '))
    for i in a:
        k = int(ord(i))
        i = chr(k+n)
        if k+n > 1103:
            i = chr((k - 1103) + 1072+n)
        b += i
    return print(b)

def dec():
    lang = input('Какой язык (русский/английский)? - ')
    b = input('Введите тест - ')
    a = int(input('Какой сдвиг? - '))
    if lang == 'русский':
        dict = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    else:
        dict = 'abcdefghijklmnopqrstuvwxyz'
    word = ''
    for i in b:
        if i in dict:
            x = dict.find(i)
            num = x - a
            word += dict[num]
        else:
            word += i
    return print(word)


def encr():
    lang = input('Какой язык (русский/английский)? - ')
    if lang == 'русский':
        russian()
    else:
        english()

what = input('Зашифровать или расшифровать текст? - ')
if what == 'расшифровать':
    dec()
else:
    encr()
