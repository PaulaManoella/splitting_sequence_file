import re

#abre o arquivo que contem as sequencias (.txt)
with open('output_5m.txt', 'r') as arquivo:
    file = arquivo.read()

"""Regex para separar os arquivos srr1 e srr2

Explicando a expressão:
-> @SRR29288960\. = string bruta, o padrão '@SRR29288960.' no inicio do cabeçalho
-> (?:[1-9]|[1-4][0-9]|50) = em resumo, qualquer numero de 1 a 50
-> \.1. = literalmente '.1', se referindo aos arquivos srr1. exemplo: @SRR29288960.1.1
-> *? = serve para capturar até um ponto específico, nesse caso, captura até encontrar o proximo cabeçalho que corresponda ao arquivo srr2
-> ?= = verifica se a sequencia passada como parametro está presente no texto, mas não o inclui na correspondencia. em resumo, verifica se o cabeçalho que corresponde ao arquivo srr2 está no texto, mas o despreza.
-> @SRR29288960\.(?:[1-9]|[1-4][0-9]|50)\.2 = representa os arquivos srr2. exemplo: @SRR29288960.1.2

"""
regex_srr1 = re.findall(r"@SRR29288960\.(?:[1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-9][0-9]{3}|[1-9][0-9]{4}|[1-9][0-9]{5}|[1-2][0-9]{6}|2500000)\.1.*?(?=@SRR29288960\.(?:[1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-9][0-9]{3}|[1-9][0-9]{4}|[1-9][0-9]{5}|[1-2][0-9]{6}|2500000)\.2)", file, flags=re.DOTALL)

regex_srr2 = re.findall(r"@SRR29288960\.(?:[1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-9][0-9]{3}|[1-9][0-9]{4}|[1-9][0-9]{5}|[1-2][0-9]{6}|2500000)\.2.*?(?=@SRR29288960\.(?:[1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-9][0-9]{3}|[1-9][0-9]{4}|[1-9][0-9]{5}|[1-2][0-9]{6}|2500000)\.1|$)", file, flags=re.DOTALL)


#cria um arquivo txt contendo as sequencias srr1
with open('SRR29288960.sra_1.txt', 'a') as arquivo:
    for i in range(len(regex_srr1)):
        file = arquivo.write(regex_srr1[i])

#cria um arquivo txt contendo as sequencias srr2
with open('SRR29288960.sra_2.txt', 'a') as arquivo:
    for i in range(len(regex_srr2)):
        file = arquivo.write(regex_srr2[i])
