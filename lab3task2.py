import random

#Функция, заполняющая список x рандомными значениями от a до b
def task2(x,a,b,randlist):
    for i in range(x):
        randlist.append(random.randint(a,b))
    return(randlist)

#Ввод x,a,b с клавиатуры, создание пустого списка
x=int(input())
a=int(input())
b=int(input())
randlist=[]

#Вывод сгенерированного списка
print(task2(x,a,b,randlist))
