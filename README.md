# Trabalho-1 -Python- (Campo-Minado-)
Feito por Rafael Alves Faria

Como jogar:
Ao iniciar o programa/jogo será exibido uma mensagem de boas vindas. Após isso, o usuário deve digitar o número de linhas e colunas para a campo minado e logo em seguida, digitar quantas minas estarão escondidas no campo.

Obs: É importante que o usuário não digite uma quantidade de bombas maior do que o tamanho do campo, caso o faça será pedido que ele informe novamente os dados pedidos antes.

Após isso, será exibido o campo minado que foi descrito pelo usuário, com todas as casas estarão preenchidas dessa forma: ' * '. 

Abaixo aparecerá o menu principal do jogo, onde o usuário pode escolher qual ação fazer. A opção ' 1 ' serve para marcar uma posição como suspeita, ' 2 ' para selecionar um espaço que pode ou não conter uma bomba e a opção ' 0 ' para "sair", fazendo com que o programa feche.

Caso o usuário escolha marcar uma posição como suspeita, lhe será pedido uma coluna e uma linha, então a posição será marcada com ' M ' ao invés de ' * '.

Agora se o usuário escolher marcar uma posição, caso a casa esteja vazia, mesmo que tenha sido marcada anteriormente, ao ser selecionada a casa mostrará um número de 0 a 8 que indicará quantas bombas estão ao redor daquele quadrado. Mas caso a posição escolhida tenha uma bomba o usuário receberá a mensagem de " Game Over " e também a matriz exibindo a localização de todas as bombas.

Para vencer o jogo, o usuário deve marcar todas as posições que tenham uma bomba como susoeita, ou seja, todas as posições com bomba devem estar como: ' M '.

Limitações:

O limite máximo para o campo minado é de 10x10.
