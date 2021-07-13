# -*- coding: utf-8 -*-

'''
Testa a classe conta bancaria
'''
from contabancaria import ContaBancaria

c1= ContaBancaria(333,'vaka','LALA')
print(c1)

c2= ContaBancaria(888,'aabb','BETO', 3500.50)
print(c2)

c1.exibeSaldo('kkkk')
c1.exibeSaldo('vaka')

print(c1)
c1.deposito(2300)
print(c1)
c1.saque(450, 'vaka')
print(c1)



    
        
        
