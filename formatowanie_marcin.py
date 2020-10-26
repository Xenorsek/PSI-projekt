zmienna = '{first} {last}'.format(first='Hoodor', last='Hodor!')
data = {'first': 'Hodoor', 'last': 'Hodor!'}
print(zmienna)
data = '{first} {last}'.format(**data)
print(data)
print('{:.4f}'.format(3.141592653589793))
print('{:8d}'.format(420))
print('{:+d}'.format(-42))