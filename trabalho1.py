from random import sample

while True :
    altura = int(input('Digite a extensão vertical do campo minado:'))                          #Usuario escolhe a altura da matriz do campo minado 
    largura = int(input('Digite a extensão horizontal do campo minado:'))                       #Usuario escolhe a largura da matriz do campo minado
    
    if altura <= 0 or largura <= 0 :  
        print('')                                                                               #Barra o processo se o usuario digitar um numero de linhas e colunas igual ou menor que 0
        print('Informe números maiores que 0')
        print('')
    
    if altura >= 10 or largura >= 10 :  
        print('')                                                                               #Barra o processo se o usuario digitar um numero de linhas e colunas igual ou menor que 0
        print('Informe números menores que 10')
        print('')
    
    else:
            
        print('')
        minas = int(input('Digite a quantidade de minas para o campo minado do campo minado.')) #Usuario escolhe a quantidade de minas do campo minado 
        print('')

        if (minas < (altura * largura)):                                                        #Se o numero de minas for menor que o numero de posições do campo, então o código continua

            colunas = []                                                                        #Colunas é basicamente a Matriz que será preenchida pelas linhas

            for i in range(altura):                                                             #Usa o valor fornecido pelo usuário para ir preenchendo a matriz com '*'
                linha = []

                for j in range(largura):
                    linha.append('*')
            
                colunas.append(linha)
            
            posicoes_minas = sample(range(largura * altura),minas)
            break
        
        else:                                                                                    #Caso o usuário digite um número de minas maior que os epaços da matriz, o programa não rodará
            print('Número de minas é maior do que o suportado no campo escolhido')










while True:
    
    minas_achadas = 0

    for i in posicoes_minas:
        linha = i// largura
        coluna = i % largura

        if colunas[linha][coluna] == 'M':
            minas_achadas += 1

    if minas_achadas == minas:
        print('Fim de Jogo. Você Venceu')
        break

    else:

        #MENU
        for i in range(altura):
            for j in range(largura):
                print(colunas[i][j], end = ' ')
            print(' ')

        print('')
        print('Digite agora o que gostaria de fazer:')
        print('1 - Marcar uma posição suspeita')
        print('2 - Escolher uma posição')
        print('0 - Sair')

        decisao = int(input('->  '))
        print('')

        if decisao == 0:
            break
        
        if decisao == 1:
            y = int(input('Digite uma coluna: '))
            x = int(input('Digite uma linha: '))

            colunas[x][y] = 'M'
        
        if decisao == 2:
            y = int(input('Digite uma coluna: '))
            x = int(input('Digite uma linha: '))

            posicao = x * largura + y


            if colunas[x][y] == 'S':
                print('Posição já averiguada')

            if colunas[x][y] == '*':

                colunas[x][y] = 'S'

            if posicao in posicoes_minas:
                
                print('')
                print('Game Over')
                print('')

                for i in posicoes_minas:
                    linha = i// largura
                    coluna = i % largura
                    colunas[linha][coluna] = "B"

                for i in range(altura):
                    for j in range(largura):
                        print(colunas[i][j], end = ' ')
                    print(' ')
                


                break