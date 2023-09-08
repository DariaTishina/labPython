from calendar import isleap
from datetime import date

#Функция для проверки года на високосность
def task1(x):
    check = isleap(x)
    return(check)

print('1 - проверить текущий год на високосность, 2 - ввести свое значение')
button = input()
if button == '1':
    today = date.today()        #Получаем текущую дату
    x = today.year              #Из нее берем только год
    print(task1(x))
elif button == '2':
    print('Введите год')
    x = int(input())
    print(task1(x))
else:
    print('Некорректное значение, повторите снова')
