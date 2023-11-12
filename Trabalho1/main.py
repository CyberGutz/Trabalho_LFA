# import AFD_jflap as jflap
from Minimizacao import Minimizacao
from Multiplicacao import Multiplicacao
from Operacoes_Conjunto import Operacoes as op
from AFD import AFD
import os
import time


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def cat(arq):
    arq = str(arq)
    if os.name == 'nt':
        os.system("notepad.exe {}".format(arq))
    else:
        os.system("cat {}".format(arq))


def continuar():
    input("Aperte qualquer tecla para continuar ...")
    clear()


if __name__ == "__main__":
    clear()
    print("*********************************************************************************************")
    print("\tDemonstração: Trabalho 1 de Linguagens formais e autômatos: ")
    print("\nPara iniciar as demonstrações utilizaremos primeiro o afd1, dado como exemplo no classroom\n")
    print("Criando afd1...\n")

    afd1 = AFD("ab")
    for i in range(1, 5):
        afd1.criaEstado(i)
    afd1.mudaEstadoInicial(1)
    afd1.mudaEstadoFinal(4, True)

    afd1.criaTransicao(1, 2, "a")
    afd1.criaTransicao(2, 1, "a")
    afd1.criaTransicao(3, 4, "a")
    afd1.criaTransicao(4, 3, "a")
    afd1.criaTransicao(1, 3, "b")
    afd1.criaTransicao(3, 1, "b")
    afd1.criaTransicao(2, 4, "b")
    afd1.criaTransicao(4, 2, "b")
    print(afd1)

    # input("\nafd1 criado com sucesso!")
    continuar()
    # Início da bateria de demonstrações
    print("*********************************************************************************************")
    print("\nDEMONSTRAÇÃO 1: Copiar Autômatos, Salvar e carregar autômatos de arquivos texto e jff (JFLAP)")
    print("\nCriando a cópia do AFD1: \n")
    copia = AFD.copiaAFD(afd1)
    print(copia)
    continuar()

    print("*********************************************************************************************")
    print("\nSalvando afd1 em um arquivo texto:")
    AFD.saveAf(afd1, "afd1")
    time.sleep(1)
    print("afd1 salvo com sucesso! Abrindo arquivo...")
    time.sleep(1)
    cat("afd1")
    continuar()

    print("*********************************************************************************************")
    print("\nCarregando o afd1 de um arquivo texto:")
    time.sleep(1)
    afaux = AFD.loadAF("afd1.txt")
    print("\nAFD carregado do arquivo:")
    print(afaux)
    continuar()

    print("*********************************************************************************************")
    print("\nSalvando afd1 em um arquivo .jff (JFLAP)")
    continuar()

    print("*********************************************************************************************")
    print("\nCarregando um afd de um arquivo .jff")
    continuar()

    print("*********************************************************************************************")
    print("\nDEMONSTRAÇÃO 2: Equivalências de Estados e Minimização")
    print("Vamos criar agora o estado 5 no afd1: \n")
    afd1.criaEstado(5)
    afd1.criaTransicao(5, 1, "a")
    afd1.criaTransicao(5, 4, "b")
    print(afd1)
    continuar()

    print("*********************************************************************************************")
    print("\nO estado 5 leva com 'a' ao estado 1 e com 'b' ao estado 4.")
    print("Perceba que essas são as mesma transições do estado 2, portanto ambos devem ser trivialmente equivalentes")
    print("\n\t 5 é equivalente ao estado 2?")
    print("Resposta do programa: ", Minimizacao.stateEq(afd1, 2, 5))
    continuar()

    print("*********************************************************************************************")
    print("\nO estado 5, portanto não pode ser igual ao estado 1, pois com o caracter 'b' o estado 5 leva ao estado 4 e o estado 1 leva ao estado 3.")
    print("Os estados 3 e 4 são trivialmente não equivalentes, uma vez que 4 é um estado final e 3 não.")
    print("Logo, 5 e 1 não podem ser equivalentes")
    print("\n\t5 é equivalente a 1?")
    print("\nResposta do programa: ", Minimizacao.stateEq(afd1, 1, 5))
    continuar()

    print("*********************************************************************************************")
    print("\nCriamos agora os estados 6 e 7.\n")
    afd1.criaEstado(6)
    afd1.criaTransicao(6, 2, "a")
    afd1.criaTransicao(6, 2, "b")
    afd1.criaEstado(7)
    afd1.criaTransicao(7, 5, "a")
    afd1.criaTransicao(7, 5, "b")
    print(afd1)
    continuar()

    print("*********************************************************************************************")
    print("\nO estado 6 com ambos os símbolos do alfabeto leva ao estado 2.")
    print("O estado 7 com ambos os símbolos do alfabeto leva ao estado 5.")
    print("Portanto, como 5 e 2 são equivalentes, 6 e 7 também devem ser:")
    print("\n\t6 é equivalente a 7?")
    print("\nResposta do programa: ", Minimizacao.stateEq(afd1, 6, 7))
    continuar()

    print("*********************************************************************************************")
    print("\nCriamos agora os estados 8 e 9.\n")
    afd1.criaEstado(8)
    afd1.criaTransicao(8, 6, "a")
    afd1.criaTransicao(8, 5, "b")
    afd1.criaEstado(9)
    afd1.criaTransicao(9, 7, "a")
    afd1.criaTransicao(9, 1, "b")
    print(afd1)
    continuar()

    print("*********************************************************************************************")
    print("\nO estado 8 com 'a' leva ao estado 6 e com 'b' leva ao estado 5.")
    print("O estado 9 com 'a' leva ao estado 7 e com 'b' leva ao estado 1.")
    print("Os estados 7 e 6 são equivalentes, porém os estados 1 e 5 não, logo 8 e 9 não podem ser equivalentes")
    print("\n\t8 é equivalente a 9?")
    print("\nResposta do programa: ", Minimizacao.stateEq(afd1, 6, 9))
    continuar()

    print("*********************************************************************************************")
    print("\nSabendo agora das relações de equivalência (6 == 7 e 2 == 5), podemos agora minimizar o autômato")
    print("afd1 antes da minimização: \n")
    print(afd1)
    print("\nafd1 depois da minimização: \n")
    Minimizacao.minimizacao(afd1)
    print("\nPerceba também que os estados 8 e 9 também foram removidos, por mais que não sejam equivalentes")
    print("Isso acontece porque 8 e 9 não eram atingidos por nenhum outro estado, o que os torna irrelevantes")
    print(afd1)
    continuar()

    print("*********************************************************************************************")
    print("\nDEMONSTRAÇÃO 3: Equivalência de Autômatos")
    print("Para essa demonstração, vamos utilizar 3 AFD's bem simples:")
    af2 = AFD('ab')
    af2.criaEstado(1, True)
    af2.criaEstado(2, False, True)
    af2.criaTransicao(1, 2, 'b')
    print("AF2: \n{}".format(af2))
    continuar()

    print("*********************************************************************************************\n")
    af3 = AFD('abc')
    af3.criaEstado(1, True)
    af3.criaEstado(2, False, True)
    af3.criaTransicao(1, 2, 'b')
    print("AF3: \n{}".format(af2))
    continuar()

    print("*********************************************************************************************\n")
    af4 = AFD('abc')
    af4.criaEstado(1, True)
    af4.criaEstado(2)
    af4.criaEstado(3, False, True)
    af4.criaTransicao(1, 2, 'b')
    af4.criaTransicao(2, 3, 'a')
    print("AF4: \n{}".format(af4))
    continuar()

    print("*********************************************************************************************")
    print("\nA equivalência de autômato nos diz que se ambos os estados iniciais dos autômatos são equivalentes, os autômatos também são equivalentes.")
    print("Desse modo, podemos ver que o af2 é equivalente ao af3, pois, embora af3 tenha um alfabeto diferente, ambos estados iniciais são equivalentes.")
    print("Vejamos melhor esse processo: ")
    print("Primeiro, devemos concatenar os autômatos: \n")
    afconcatenado = Minimizacao.concatAF(af2, af3)
    print("\n\tAF23: \n{}".format(afconcatenado))
    print("Com os dois autômatos concatenados, podemos verificar se ambos os seus estados iniciais são iguais, com a verificação de estados:")
    print("\n\tAF2 é equivalente ao AF3?")
    print("\nResposta do programa: ", Minimizacao.afEq(af2, af3))
    continuar()

    print("*********************************************************************************************")
    print("\nAgora veremos com os AF2 e AF4.")
    afconcatenado = Minimizacao.concatAF(af2, af4)
    print("\n\tAF24: \n{}".format(afconcatenado))
    print("Com os dois autômatos concatenados, podemos verificar se ambos os seus estados iniciais são iguais, com a verificação de estados:")
    print("\n\tAF2 é equivalente ao AF4?")
    print("\nResposta do programa: ", Minimizacao.afEq(af2, af4))
    print("\nComo podemos ver, o AF2 e AF4 não são equivalentes, pois seus estados iniciais são diferentes.")
    print("O inicial de AF2 leva a um estado final, e o inicial de AF4 leva a um estado que não é final, logo os estados não são equivalentes.")
    continuar()

