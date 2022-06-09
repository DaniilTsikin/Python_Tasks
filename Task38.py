# Напишите программу, которая удаляет из текста все слова, содержащие "абв"

text = 'абваьвр айпшгцпаг абвалодал оавлра абвылоа блоавыба рлшрабв'
print('text:', text)

text_word = text.split()
print('text_word:', text_word)

find = 'абв'

new_text = []

for i in text_word:
    if find not in i:
        new_text.append(i)
print('new_text:', new_text)

# Сбор новой строки через /join разделитель - пробел
text_2 = ' '.join(new_text)
print('Вывод:', text_2)