#Создание функции для сравнения первых/последних чисел
def task2(x,y):
    if x[0] == y[0] or x[len(x)-1] == y[len(y)-1]:
        return True
    else:
        return False

#Создание пустых списков
x=[]
y=[]

#Заполнение первого списка
print ('Заполните первый список числами через enter, затем введите stop')
while True: 
    el = input ()
    if el == 'stop':
        break
    x.append(el)
    el = None

#Заполнение второго списка
print ('Заполните второй список числами через enter, затем введите stop')
while True: 
    el = input ()
    if el == 'stop':
        break
    y.append(el)
    el = None

#Вывод результата - True или False
print (task2(x,y))
