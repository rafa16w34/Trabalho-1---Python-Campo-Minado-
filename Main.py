from random import sample    #Usei essa bibliooteca para que pudesse aleatorizar as posições das bombas na matriz, salvando os índices de cada posição da bomba em uma lista.

print('Bem vindo ao Campo Minado. Para jogar siga as instruções informadas no terminal ou no README.\nFeito por Rafael Alves Faria.\n')     #Simples mensagem inicial para o usuário.

while True :

    try:
        altura = int(input('Digite a extensão vertical do campo minado (Tamanho mínimo: 1 e máximo: 10): '))                          #Usuário escolhe a altura da matriz do campo minado.
        largura = int(input('Digite a extensão horizontal do campo minado (Tamanho mínimo: 1 e máximo: 10): '))                       #Usuário escolhe a largura da matriz do campo minado.
    
        if altura <= 0 or largura <= 0 :  

            print('\nInforme números maiores que 0.\n')                                             #Barra o processo se o usuário digitar um numero de linhas ou colunas igual ou menor que 0.

        
        if altura > 10 or largura > 10 :  

            print('\nInforme números menores que 10.\n')                                            #Barra o processo se o usuário digitar um numero de linhas ou colunas igual ou menor que 0.

        
        
        else:

            try:   
                
                minas = int(input('\nDigite a quantidade de minas para o campo minado do campo minado: ')) #Usuário escolhe a quantidade de minas do campo minado.
                


                if (minas < (altura * largura)) and minas > 0:                                                        #Se o número de minas for menor que o número de posições do campo, então o jogo continua normalmente.

                    colunas = []                                                                        #A lista "Colunas" é basicamente a Matriz que será preenchida pelas linhas, já que as colunas são sempre printadas primeiro.

                    for i in range(altura):                                                             #Usa o valor fornecido pelo usuário para ir preenchendo a matriz com '*' que simboliza uma posição ainda não jogada ou marcada.
                        linha = []

                        for j in range(largura):
                            linha.append('*')
                    
                        colunas.append(linha)
                    
                    posicoes_minas = sample(range(largura * altura),minas)
                    break
                
                elif (minas >= (altura * largura)):                                                                                   #Caso o usuário digite um número de minas maior que os epaços da matriz, o jogo não irá aceitar.
                    print('\nNúmero de minas é maior do que o suportado no campo escolhido.\n')

                elif (minas <= 0):
                    print('\nO número de minas deve ser maior que 0.\n')
            
            except ValueError:
                print(f'\nO número de minas no campo deve ser um número inteiro.\n')
    
    except ValueError:                                                                               #Caso o usuário não digite um caractere diferente de um número inteiro.
        print(f'\nA altura e largura devem ser números inteiros.\n')





def contar_bombas_vizinhas(x, y, largura, altura, posicoes_minas):                              #Função que conta quantas minas estão presentes ao redor da posição escolhida pelo usuário, recebe as coordenadas da posição escolhida, o tamanho da matriz (altura e largura) e a lista com o indíce da posição das minas.
    total_bombas_vizinhas = 0
    
    for posicao_horizontal in [-1,0,1] :
        for posicao_vertical in [-1,0,1]:
            
            if posicao_horizontal == 0 and posicao_vertical == 0:                               #Se isso for verdade estaremos olhando para a própria posição escolhida, o que não faz sentido, pois caso se escolha a bomba o jogo deve acabar.
                continue                                                                        #Por isso deve-se fazer com que ignoremos essa possibilidade.
            
            vizinho_x = x + posicao_horizontal
            vizinho_y = y + posicao_vertical

            if (0 <= vizinho_x < altura) and (0 <= vizinho_y < largura):                        #Não permite que acesse uma posição fora da matriz.
                indice = vizinho_x * largura + vizinho_y                                        #Salva a posição em um indíce para que possa ser comparado com a lista da localização das bombas, que estão salvas em indíces.

                if indice in posicoes_minas:                                                    #Se o indíce da posição do vizinho for equivalente a presente na lista das bombas, então será acrescido um no total na varável "total_bombas_vizinhas".
                    total_bombas_vizinhas += 1

    return total_bombas_vizinhas


def printar_campo_minado(altura,largura,perdeu):                                    #A função que printa o campo minado.
    numero_colunas = []                                                             #Uma lista que salva quantas colunas o campo tem, para que seja exibido e fique mais intuitivo ao usuário na hora de escolher a posição.
    numero = 0

    if perdeu == True:                                                              #Somente será verdade se perder o jogo.
        for i in posicoes_minas:                                                    #Ao perder será exibido a matriz completa mostrando a localização de cada bomba, representadas por 'B'.
            linha = i// largura
            coluna = i % largura
            colunas[linha][coluna] = "B"

    for i in range(largura):                 #Preenche a lista da "numero_colunas" com o número de colunas.
        numero_colunas.append(numero)
        numero = numero + 1

    for i in range(numero):     #Printa cada posição da lista, enumerando cada coluna.

        if i == 0:
            print('  ',end='')

        print(f' {numero_colunas[i]}',end='')
    
    print(' ')

    for i in range(altura):        #Printa a matriz do campo minado de forma formatada para melhor visualização do usuário.
        for j in range(largura):

            if (j == 0):
                print(f'[{i}]',end = '')

            print(f'{colunas[i][j]}', end = ' ')
        print(' ')

while True:                     #Vai repetir esse loop ao até o usuário perder ou ganhar no jogo.
    
    minas_achadas = 0           #Variável que armazena quantas bombas foram marcadas pelo usuário.

    for i in posicoes_minas:    #Transforma os números da aleatórios da lista de bombas em posições para a matriz do campo minado.
        linha = i// largura
        coluna = i % largura

        if colunas[linha][coluna] == 'M':          #Verifica se a posição de alguma bomba está marcada com 'M' ou seja, se o usário marcou ela como suspeita.
            minas_achadas += 1                     #Caso tenha ele acrescenta em 1 na variável de minas achadas.

    if minas_achadas == minas:                     #Se o usuário marcar todas as minas como posições suspeitas o jogo acaba e ele vence.
        print('Fim de Jogo. Você Venceu')
        break

    else:                                          #Caso ele não tenha achado todas as minas, então o jogo continua.

        #MENU PRINCIPAL:

        perdeu = False                                      #Inicia a variável perdeu como False, já que o jogo ainda não acabou.

        print('')

        printar_campo_minado(altura,largura,perdeu)         #Função de printar o campo minado, recebe a altura, a largura e a varíável booleana "perdeu".


        print('\nDigite agora o que gostaria de fazer:\n1 - Marcar uma posição suspeita\n2 - Escolher uma posição\n0 - Sair\n')      #Menu simples em loop que mostra as opções que o usuário tem.

        try:                                                    #Verifica se o usuário não irá digitar algo diferente de um número inteiro.
            decisao = int(input('->  '))                        #Recebe a opção escolhida pelo usuário.
            print('')

            if decisao == 0:                                    #Se o usuário escolher 0 o programa se encerra.
                break

            if decisao == 1:                                    #Se o usuário escolher 1 ele deve então escolher uma posição da matriz para marca-la como suspeita, ou seja, irá substituir '*' por 'M' dentro da matriz.
                y = int(input('Digite uma coluna: '))
                x = int(input('Digite uma linha: '))

                if (x < largura) and not (x > largura) and (y < altura) and not (y > altura):       #Verifica se a posição escolhida está realmente dentro da matriz.

                    if colunas[x][y] == '*':
                        colunas[x][y] = 'M'

                    print('')
                
                else:                                                                              #Se for escolhida uma posição fora da matriz será pedido ao usuário que ele escolha uma posição válida.
                    
                    print(f'\nSelecione uma posição dentro da matriz [{largura}][{altura}]\n')
 

            if decisao == 2:                                    #Se o usuário digitar 2 ele deve escolher uma posição para jogar.
                y = int(input('Digite uma coluna: '))
                x = int(input('Digite uma linha: '))

                print('')
            
                if (x < largura) and not (x > largura) and (y < altura) and not (y > altura):       #Verifica se a posição escolhida está realmente dentro da matriz.
                    posicao = x * largura + y                                                       #Calcula o indíce da posição, para que possa comparar com os das bombas.

                    if colunas[x][y] == '*' or colunas[x][y] == 'M':                                                        #Se a posição escolhida for '*' ele irá executar a função "contar_bombas_vizinhas" e vai substituir o '*' pelo valor retornado da função, ou seja, o número de bombas ao redor da posição escolhida.

                        total_bombas_vizinhas = contar_bombas_vizinhas(x,y,largura,altura,posicoes_minas)
                        colunas[x][y] = str(total_bombas_vizinhas)

                    if posicao in posicoes_minas:                                                   #Se o indíce da posição escolhida pelo usuário estiver presente na lista das posições de bomba, então ele terá escolhido uma bomba e por isso irá perder o jogo.
                        
                        perdeu = True

                        
                        print('\nGame Over\n')
                        

                        printar_campo_minado(altura,largura,perdeu)                                 #Nesse caso, agora o campo mostra as bombas que estavam escondidas, pois a variável perdeu = True.
                        
                        print(' ')
                        break
                else:                                                                              #Se for escolhida uma posição fora da matriz será pedido ao usuário que ele escolha uma posição válida.
                    
                    print(f'\nSelecione uma posição dentro da matriz [{largura}][{altura}]\n')
                    
        
        except ValueError:                                                                         #Caso o usuário digite um caractere que não seja um inteiro.
            print(f'\nDigite umas das opções mostradas no Menu.\n')
