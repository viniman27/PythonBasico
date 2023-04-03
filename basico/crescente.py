# for n in range(10):
#     print(n)
    
# for n in range(5,15):
#     print(n)

# for n in range(15,5,-1):
#     print(n)

# x = 0

# while x<=15:
#     print(x)
#     x = x + 1

qtd = 0
soma = 0
media = 0 
valor = float(input('valor: '))

while(valor > 0.0):
        soma = soma + valor
        qtd = qtd + 1
        
        #input dos valores
        valor = float(input('valor: '))
        
media = soma/qtd

print('soma: ', soma)
print('qtd: ', qtd)
print('media: ', media)