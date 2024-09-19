def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding = 'utf-8')
    for i, string in enumerate(strings):
        strings_positions[(i + 1, file.tell())] = string
        file.write(str(string) + '\n')
    file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test_7,2.txt', info)
for elem in result.items():
  print(elem)