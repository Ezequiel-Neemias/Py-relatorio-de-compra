compra = list()
classe = dict()
produtos = list()

while True:
    classe.clear()
    produtos.clear()
    classe['Produtos:']= str(input('Digite a classe dos produtos: '))
    tot= int(input(f'Quantos produtos em {classe["Produtos:"]} voce comprou? '))
    classe['Qtd:'] = tot
    for c in range (tot):
        produtos.append(float(input(f'    Qual o preço do produto {c} ?')))
    classe['Total R$:'] = sum(produtos)
    classe['Preços:']= produtos[:]
    compra.append(classe.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]')).upper()[0]
        if continua in 'SN':
            break
        print('Erro!! Por favor responda apenas com S ou N.')
    if continua == 'N':
        break
print('--'*40)
print('Cod:',' ', end='')
for i in classe.keys():
    print(f'{i:<15}', end='')
print()
print('--'* 40)
for k,v in enumerate (compra):
    print(f'{k:>3}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*40)
while True:
    busc = int(input('Mostrar dados com detalhe de qual classe de produtos? (999 para parar.) '))
    if busc == 999:
        break
    if busc >= len(compra):
        print(f'Erro!! Não existe nenhuma classe de produto com o código {busc}!')
    else:
        print()
        print(f'   DETALHE DA CLASSE DA COMPRA: {compra[busc]["Produtos:"]}')
        for i, p in enumerate(compra[busc]['Preços:']):
            print(f' => O produto {i} Custa {p} Reais.')
        print(f'  Total: R${classe["Total R$:"]}')
    print('--'*40)
print('  => VOLTE SEMPRE!!!   ')



