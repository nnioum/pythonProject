# Шифр Цезаря
def english():
    b = ''
    a = input('Введите тест - ')
    n = int(input('Какой сдвиг?'))
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
    n = int(input('Какой сдвиг?'))
    for i in a:
        k = int(ord(i))
        if (160 <= k <= 175) or (224 <= k <= 239):
            i = chr(k+n)
            if k+n > 175:
                i = chr((k - 175) + 223)
            elif k+n > 239:
                i = chr((k+n - 239) + 159)
        b += i
    return print(b)

def dec():
    lang = input('Какой язык? - ')
    b = input('Введите тест - ')
    a = int(input('Какой сдвиг?'))
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
    lang = input('Какой язык? - ')
    if lang == 'русский':
        russian()
    else:
        english()

what = input('Что делать? - ')
if what == 'расшифровать':
    dec()
else:
    encr()

# # На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# # Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# # Строчные буквы при этом остаются строчными, а прописные – прописными.
# a = input()
# b = ''
# for i in a:
#     if i in ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM':
#         b += i
# b = b.split()
# a = a.split()
# k = ''
# d = -1
# for i in a:
#     n = len(b[d+1])
#     for j in i:
#         s = ord(j)
#         if 97 <= s <= 122:
#             j = chr(s+n)
#             if s+n > 122:
#                 j = chr((s+n-122)+96)
#         elif 65 <= s <= 90:
#             j = chr(s+n)
#             if s+n > 90:
#                 j = chr(s+n-90+64)
#
#         k += j
#     k += ' '
#     d += 1
# print(k)