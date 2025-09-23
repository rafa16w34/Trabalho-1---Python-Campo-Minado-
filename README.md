# Trabalho-1---Python-Campo-Minado-
Feito por Rafael Alves Faria

Ao iniciar o programa/jogo será exibido uma mensagem de boas vindas seguidas do nome do criador, eu mesmo. Após isso, o usuário deve digitar o número de linhas e colunas para a matriz/campo minado e logo em seguida, digitar quantas minas estarão escondidas no campo.

Obs: É importante que usuário saiba que o tamanho máximo da matriz é 10x10, além disso não será aceito uma quantidade de bombas maior do que o tamanho do campo.

Após isso, será exibido o campo que foi descrito pelo usuário, sendo que primeiramente todas as casas estarão preenchidas com ' * '. Abaixo aparecerá um menu onde o usuário pode escolher digitar ' 1 ' para marcar uma posição como suspeita; ' 2 ' para selecionar um espaço que pode ou não conter uma bomba, ou escolher ' 0 ' e "sair", fazendo com que o programa feche.

Caso o usuário escolha marcar uma posição como suspeita, lhe será pedido uma coluna e uma linha, então a posição será marcada com ' M ' ao invés de ' * '.

Agora se o usuário escolher marcar uma posição, caso a casa esteja vazia, mesmo que tenha sido marcada anteriormente, ao ser selecionada a casa mostrará um número de 0 a 8 que indicará quantas bombas estão ao redor daquele quadrado. Mas caso a posição escolhida tenha uma bomba o usuário receberá a mensagem de " Game Over " e também a matriz exibindo a localização de todas as bombas.
