def task2(x,y):
    if x[0] == y[0] or x[len(x)-1] == y[len(y)-1]:
        return True
    else:
        return False

x=[]
y=[]
print ('Заполните первый список числами, затем введите stop')
while True: 
    el = input ()
    if el == 'stop':
        break
    x.append(el)
    el = None
print ('Заполните второй список числами, затем введите stop')
while True: 
    el = input ()
    if el == 'stop':
        break
    y.append(el)
    el = None
print (task2(x,y))
