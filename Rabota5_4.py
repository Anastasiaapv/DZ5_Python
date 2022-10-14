#  Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open('file_encode.txt', 'w') as data:
    data.write('aaaaaaabbbbbbtttttccccccccc')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = coding(decoded_string)
    file.write(encoded_string)

print('Начальный текст: \t' + decoded_string)
print('Текст после кодировки: \t' + coding(decoded_string))
print(f"Текст после дешифровки: {decoding(coding(decoded_string))}")