# ----------------------Parte das operações------------------------
def parte_logica(operacao, primeiro, segundo):
# faz a operação de produto cartesiano!
    if operacao == "C":
        resultado = [(x,y)for x in primeiro for y in segundo]
        # for i in range(len(primeiro)):
        #     for j in range(len(segundo)):
        #         resultado.append((primeiro[i], segundo[j]))
        print('Produto Cartesiano: conjunto 1 {',primeiro,'}, conjunto 2 {', segundo,'}. Resultado: {',resultado,'}')
# faz a operação de União!
    elif operacao == "U":
        resultado = list(set(primeiro) | set(segundo))
        # for i in range(len(primeiro)):  
        #     for j in range(len(segundo)):
        #         if primeiro[i] not in resultado:
        #             resultado.append(primeiro[i])
        #         if segundo[j] not in resultado:
        #             resultado.append(segundo[j])
        print('União: conjunto 1 {',primeiro,'}, conjunto 2 {', segundo,'}. Resultado: {',resultado,'}')

# faz a operação de diferença!
    elif operacao == "D":
        resultado = list(set(primeiro) - set(segundo))
        # for i in range(len(primeiro)):
        #     if primeiro[i] not in segundo:
        #         resultado.append(primeiro[i])
        print('Diferença: conjunto 1 {',primeiro,'}, conjunto 2 {', segundo,'}. Resultado: {',resultado,'}')

# faz operação de intersecção!
    elif operacao == "I":
        resultado = list(set(primeiro) & set(segundo))
        # for i in range(len(primeiro)):
        #     for j in range(len(segundo)):
        #         if primeiro[i] == segundo[j]:
        #             resultado.append(primeiro[i])
        print('Intersecção: conjunto 1 {',primeiro,'}, conjunto 2 {', segundo,'}. Resultado: {',resultado,'}')

# --------------------PARTE FUNCIONAL --------------------------
# primeira linha do arquivo
with open("conjunto.txt", "r")as primeLinha:
    primeiraLinhaDoCodigo = int(primeLinha.readline().rstrip('\n'))
    
# como ler uma linha desejada
with open("conjunto.txt", "r")as conjunto:
    linhas = conjunto.readlines()
    for i in range(1, len(linhas),3):
        operacao = linhas[i].rstrip('\n') #vai ler a linha da operação
        dominio = linhas[i + 1].rstrip('\n') #vai ler a linha do primeiro conjunto
        contraDominio = linhas[i + 2].rstrip('\n')#vai ler a linha do segundo conjunto
        parte_logica(operacao, dominio.split(', '), contraDominio.split(', ')) #separa os itens pelo (virgula e espaço): ', '

# # 1- ver quantas operações eu vou ter 
# print(primeiraLinhaDoCodigo)
# # 2 - qual a operação terei que fazer
# print(operacao)
# # 2.1 - separar o dominio em uma variavel
# print(dominio)
# # 2.2 - separa o contradominio em variavel
# print(contraDominio)
# # 3 - printar com o resultado na formataçao correta!