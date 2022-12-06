# запись в файл
with open('resources/example.txt', 'w') as f:
    f.write('Hello world!\nWorld hello\nabc')

# чтение файла
with open('resources/example.txt') as f:
    for row in f:
        print(row)

# запись первый раз, в существующий файл уже не получится записать с помощью x
# with open('example1.txt', 'x') as f:
#     f.write('Hello world!\nWorld hello')

# создание если не существует и дописывание в конец файла если существует
with open('resources/example_a', 'a') as f:
    f.write('A')

with open('resources/example.txt') as f:
    text = f.read()
    assert 'abc' in text
