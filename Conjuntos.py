# ----------------------Parte das operações------------------------
def parte_logica(operacao, primeiro, segundo):
    try:
        if operacao == "C" or operacao == "U" or operacao == "D" or operacao == "I":
    
            match operacao:
                # faz a operação de produto cartesiano!
                case "C":
                    resultado = str([(x,y)for x in primeiro for y in segundo])
                    print('Produto Cartesiano: conjunto 1 {',", ".join(primeiro).replace("'", ""),
                    '}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',
                    resultado.replace("'", "").replace("[","").replace("]",""),'}')
                # faz a operação de União!
                case "U":
                    resultado = list(set(primeiro) | set(segundo))
                    print('União: conjunto 1 {',", ".join(primeiro).replace("'", ""),
                    '}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',
                    ", ".join(resultado).replace("'", ""),'}')
                    # .join adiciona o espaço entre os elementos e o replace() tira os elementos antes da virgula e\
                    #  \n substitui pelo dps da virgula

                # faz a operação de diferença!
                case "D":
                    resultado = list(set(primeiro) - set(segundo))
                    print('Diferença: conjunto 1 {',", ".join(primeiro).replace("'", ""),
                    '}, conjunto 2 {',", ".join(segundo).replace("'", ""),'}. Resultado: {',
                    ", ".join(resultado).replace("'", ""),'}')

                # faz operação de intersecção!
                case "I":
                    resultado = list(set(primeiro) & set(segundo))
                    print('Intersecção: conjunto 1 {',", ".join(primeiro).replace("'", ""),
                    '}, conjunto 2 {', ", ".join(segundo).replace("'", ""),'}. Resultado: {',
                    ", ".join(resultado).replace("'", ""),'}')
        else:
            raise ValueError("O arquivo possui erro!")
    except FileExistsError as Error:
       Error
# --------------------PARTE FUNCIONAL --------------------------
#verifica se o arquivo existe
arquivo = input("Insira o nome do arquivo que deseja colocar, mas não coloque o complemento '.txt'!\
                \nAssim como o exemplo (conjunto) : ")
arquivo += ".txt"
try:
    # primeira linha do arquivo
    with open(arquivo, "r")as primeLinha:
        primeiraLinhaDoCodigo = (primeLinha.readline().rstrip('\n'))
        primeiraLinhaDoCodigo = int(primeiraLinhaDoCodigo)
    # como ler uma linha desejada
    with open(arquivo, "r")as conjunto:
        linhas = conjunto.readlines()
        for i in range(1,(primeiraLinhaDoCodigo * 3),3):
            operacao = linhas[i].rstrip('\n') #vai ler a linha da operação 
            dominio = linhas[i + 1].rstrip('\n') #vai ler a linha do primeiro conjunto
            contraDominio = linhas[i + 2].rstrip('\n')#vai ler a linha do segundo conjunto
            parte_logica(operacao, dominio.split(', '), contraDominio.split(', ')) #separa os itens pelo (virgula e espaço): ', '
except FileNotFoundError:
    print(FileNotFoundError, "O nome do arquivo inserido não foi encontrado!")