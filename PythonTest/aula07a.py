#nome= input('Qual é o seu nomw')
#print('prazer em te conhecer {:20} !'.format(nome))

n1 = int(input('Um valor'))
n2 = int(input('Outro valor: '))
s = n1 + n2
n = n1 * n2
d= n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma vale {}, \n o produto é {} e a divisao e {}',format( s, n, d, end=' '))
print('Divisao inteira {} e potencia {}'.format(di, e))