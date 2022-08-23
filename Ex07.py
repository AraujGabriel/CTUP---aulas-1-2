n1 = float(input('valor do produto 1:'))
n2 = float(input('valor do produto 2:'))
n3 = float(input('valor do produto 3:'))
n4 = float(input('valor do produto 4:'))
n5 = float(input('valor do produto 5:'))
m = n1+n2+n3+n4+n5
print('valor da compra:', m)
p = float(input('insira o pagamento:'))
t = p - m
print( 'troco do cliente:', t)