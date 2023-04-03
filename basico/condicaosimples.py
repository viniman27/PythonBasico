A = int(input('A: '))
B = int(input('B: '))


#calculo media

media = A + B/2

if (media > 7):
    print('passou, tua media foi: ', media)
else:
    print('deu nao campeao, tua media foi: \n', media)


# teste básico de if

if (A>B):
    aux = A
    A=B
    B= aux
else:
    print('sai daqui moss, mudou nao')




print('A novo:', A)
print('B novo:', B)

