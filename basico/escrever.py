arquivo = open('arqText.txt','w')

arquivo.write('curso python \n')
arquivo.write('aula prática \n')
arquivo.close()


# Leitura do arquivo texto

leitura = open('arqText.txt','r')

print(leitura.read())
leitura.close