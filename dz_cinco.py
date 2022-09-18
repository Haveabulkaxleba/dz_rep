# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
line = 'Итс абвтайм ту навести суетуабв'
result = ' '.join(filter(lambda x: 'абв' not in x, line.split()))
print(result)

with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(result)