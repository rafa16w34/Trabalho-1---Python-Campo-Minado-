# Trabalho 1 de Python (<ins> Campo Minado </ins>)
<ins> Feito por Rafael Alves Faria </ins>

## Como jogar:

Ao iniciar o programa/jogo será exibido uma mensagem de boas vindas. Após isso, o usuário deve digitar o número de linhas e colunas para a campo minado e logo em seguida, digitar quantas minas estarão escondidas no campo.

> O jogador indica o tamanho do campo minado (no maximo 10 x 10), bem como o número de minas a serem escondidas

*Obs:* É importante que o usuário não digite uma quantidade de bombas maior do que o tamanho do campo, caso o faça será pedido que ele informe novamente os dados pedidos antes.

Após isso, será exibido o campo minado que foi descrito pelo usuário, com todas as casas estarão preenchidas dessa forma: ' * '. 
> [...] marca todas as posições com o símbolo '*'

Abaixo aparecerá o menu principal do jogo, onde o usuário pode escolher qual ação fazer:
* A opção ' 1 ' serve para marcar uma posição como suspeita;
  
  > [...] marcar uma posição como mina (ficando marcada com a letra 'M')
* Se escolher a opção ' 2 ' deve selecionar um espaço para abrir, que pode ou não conter uma bomba

  > [...] abrir uma posição (ficando marcada com a quantidade de minas vizinhas nas 8 posições vizinhas)
* E por último a opção ' 0 ' para "sair", fazendo com que o programa feche.

Caso o usuário escolha marcar uma posição como suspeita, lhe será pedido uma coluna e uma linha, então a posição será marcada com ' M ' ao invés de ' * '.

Agora se o usuário escolher marcar uma posição, caso a casa esteja vazia, mesmo que tenha sido marcada anteriormente, ao ser selecionada a casa mostrará um número de 0 a 8 que indicará quantas bombas estão ao redor daquele quadrado. 

Caso a posição escolhida tenha uma bomba o usuário receberá a mensagem de " Game Over " e também a matriz exibindo a localização de todas as bombas.
> O jogador perde se abrir uma posição que contenha uma mina

Para vencer o jogo, o usuário deve marcar todas as posições que tenham uma bomba como suspeita, ou seja, todas as posições com bomba devem estar como: ' M '.
> O jogador vence se conseguir marcar com a letra 'M' todas as posições corretas

## Limitações:

* O limite máximo para o campo minado é de 10x10.

* Caso o usuário escolha não jogar e simplesmente marcar todas as casas como suspeitas, eventualmente irá vencer o jogo, já que basta as casas com bombas estarem marcadas como suspeitas para que se vença.
