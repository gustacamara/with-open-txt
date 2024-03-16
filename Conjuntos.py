# ----------------------Parte das operações------------------------
def parte_logica(operacao, primeiro, segundo):
# faz a operação de produto cartesiano!
    if operacao == "C":
        resultado = [(x,y)for x in primeiro for y in segundo]
        print('Produto Cartesiano: conjunto 1 {',", ".join(primeiro).replace("'", ""),'}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',resultado,'}')
# faz a operação de União!
    elif operacao == "U":
        resultado = list(set(primeiro) | set(segundo))
        print('União: conjunto 1 {',", ".join(primeiro).replace("'", ""),'}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',", ".join(resultado).replace("'", ""),'}')

# faz a operação de diferença!
    elif operacao == "D":
        resultado = list(set(primeiro) - set(segundo))
        print('Diferença: conjunto 1 {',", ".join(primeiro).replace("'", ""),'}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',", ".join(resultado).replace("'", ""),'}')

# faz operação de intersecção!
    elif operacao == "I":
        resultado = list(set(primeiro) & set(segundo))
        print('Intersecção: conjunto 1 {',", ".join(primeiro).replace("'", ""),'}, conjunto 2 {', ", ".join(segundo).replace("'", ""),'}. Resultado: {',", ".join(resultado).replace("'", ""),'}')

# --------------------PARTE FUNCIONAL --------------------------
# primeira linha do arquivo
with open("conjunto.txt", "r")as primeLinha:
    primeiraLinhaDoCodigo = (primeLinha.readline().rstrip('\n'))
    primeiraLinhaDoCodigo = int(primeiraLinhaDoCodigo)
# como ler uma linha desejada
with open("conjunto.txt", "r")as conjunto:
    linhas = conjunto.readlines()
    for i in range(1,(primeiraLinhaDoCodigo * 3),3):
        operacao = linhas[i].rstrip('\n') #vai ler a linha da operação 
        dominio = linhas[i + 1].rstrip('\n') #vai ler a linha do primeiro conjunto
        contraDominio = linhas[i + 2].rstrip('\n')#vai ler a linha do segundo conjunto
        parte_logica(operacao, dominio.split(', '), contraDominio.split(', ')) #separa os itens pelo (virgula e espaço): ', '
