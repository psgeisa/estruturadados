##################
# Programa sequencial
######################

# Aplicando desconto de maneira simples
def registrar_venda():
    preco = float(input('Informe o preço do produto: '))
    qtd = int(input('Informe a quantidade do produto: '))
    desconto = float(input('Desconto percentual a ser aplicado: '))
    total = preco * qtd
    total_com_desconto = total - (total * (desconto/100.0))
    print('Valor total com desconto: ', total_com_desconto)

registrar_venda()

# Aplicando desconto por estrutura de seleção
def registrar_2venda():
    preco = float(input('Informe o preço da compra: '))
    qtd = int(input('Informe a quantidade desejada: '))
    total = preco * qtd
    if total > 150.0:
        total_com_desconto = total - (total * 0.15)
    else: 
        total_com_desconto = total - (total * 0.05)
    print('O valor total com desconto é: ', total_com_desconto)
registrar_2venda()

# Aplicando desconto por estrutura de seleção composta (if, elif, else)
def registrar_3compra():
    preco = float(input('Informe o preco do produto: '))
    qtd = int(input('Informe a quantidade: '))
    total = preco * qtd
    if total > 150.0:
        total_com_desconto = total - (total * 0.15)
    else:
        if total > 100.0:
            total_com_desconto = total - (total * 0.10)
        else:
            total_com_desconto = total - (total * 0.05)
    print("Valor total com desconto: ", total_com_desconto)
registrar_3compra()

# Aplicando desconto por estrutura de repetição (while)
def registrar_4compra():
    preco = float(input('Informe o preço do produto: '))
    qtd = -1 # força o while executar pelo menos uma vez
    while qtd < 1:
        qtd = int(input('Informe a quantidade do produto: '))
    total = preco * qtd
    print('O valor total é: ', total)
registrar_4compra()

# Aplicando nota em provas por estrutura de repetição (for)
def registrar_notas():
    notas = []
    for i in range(1, 4): # i varia de 1 a 3
        prova = float(input('Nota da prova %d: ' % i))
        notas.append(prova)
    media = sum(notas)/len(notas)
    print("Media nas provas: %.2f" % media)
registrar_notas()
