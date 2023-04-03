def lerNotas():
    valor = float(input('valor: '))
    return valor

def resultado(n1,n2):
    
    media = (n1+n2)/2
    
    print('nota 1 :', n1)
    print('nota 2 :', n2)
    print('media: ', media, 'resultado: ', end = '')
    
    if media >= 7:
        print('aprovado')
    else:
        print('reprovado')
    
    
a = lerNotas()
b = lerNotas()

resultado(a,b)