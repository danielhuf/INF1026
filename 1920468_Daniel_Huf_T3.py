#Daniel Huf
#mat.1920468

def reajusta(minimo,maximo,preco,taxa):
    if minimo<=preco and preco<=maximo:
        novo=(1+taxa)*preco
        return (preco,novo)
    else:
        return (preco,)
    
a=reajusta(10.5,20.5,15.2,0.5)

if len(a)==1:
    print('Valor mantido:',a)
else:
    print('Valor antigo: %.2f - Valor novo: %.2f'%(a[0],a[1]))