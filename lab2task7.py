# Функция для удаления неподходящих элементов из списка
def task7(x):
    n=0
    while n<len(x):
        if (x[n] * x[n]) > 30:
            x.pop(n)
        else:
            n=n+1
    return (x)

# Создание пустого списка
x = []

# Заполнение списка
while True:
    el = input()
    el = int(el)
    if el == 000:
        break
    x.append(el)

# Создаем файл для вывода результата или используем уже существующий
with open('lab2task7.txt', 'a') as f:
    print(task7(x), file=f)
