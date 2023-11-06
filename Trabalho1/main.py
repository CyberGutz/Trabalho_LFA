from Minimizacao import Minimizacao
from AFD import AFD

if __name__ == '__main__':
    teste = AFD('ab')
    for i in range(1, 5):
        teste.criaEstado(i)

    teste.mudaEstadoInicial(1)
    teste.mudaEstadoFinal(4, True)

    teste.criaTransicao(1, 2, 'a')
    teste.criaTransicao(2, 1, 'a')
    teste.criaTransicao(3, 4, 'a')
    teste.criaTransicao(4, 3, 'a')
    teste.criaTransicao(1, 3, 'b')
    teste.criaTransicao(3, 1, 'b')
    teste.criaTransicao(2, 4, 'b')
    teste.criaTransicao(4, 5, 'b')

    teste.criaEstado(5)
    teste.criaTransicao(5, 1, 'a')
    teste.criaTransicao(5, 4, 'b')

    print(Minimizacao.stateEq(teste, 1, 5))
    print(Minimizacao.stateEq(teste, 2, 5))

    teste.criaEstado(6)
    teste.criaTransicao(6, 2, 'a')
    teste.criaTransicao(6, 2, 'b')
    teste.criaEstado(7)
    teste.criaTransicao(7, 5, 'a')
    teste.criaTransicao(7, 5, 'b')

    print(Minimizacao.stateEq(teste, 6, 7))

    teste.criaEstado(8)
    teste.criaTransicao(8, 6, 'a')
    teste.criaTransicao(8, 3, 'b')
    teste.criaEstado(9)
    teste.criaTransicao(9, 7, 'a')
    teste.criaTransicao(9, 1, 'b')

    print(Minimizacao.stateEq(teste, 8, 9))

    print(teste)

    Minimizacao.minimizacao(teste)
    print(teste)



    # # Teste Equivalência de Autômatos
    af1 = AFD('ab')
    for i in range(0, 4):
        af1.criaEstado(i)
    af1.mudaEstadoInicial(0)
    af1.mudaEstadoFinal(2, True)
    af1.criaTransicao(0, 1, 'a')
    af1.criaTransicao(0, 0, 'b')
    af1.criaTransicao(1, 2, 'a')
    af1.criaTransicao(1, 0, 'b')
    af1.criaTransicao(2, 2, 'a')
    af1.criaTransicao(2, 2, 'b')
    af1.criaTransicao(3, 3, 'a')
    af1.criaTransicao(3, 3, 'b')

    af2 = AFD('ab')
    for i in range(1, 5):
        af2.criaEstado(i)
    af2.mudaEstadoInicial(1)
    af2.mudaEstadoFinal(3, True)
    af2.criaTransicao(1, 1, 'a')
    af2.criaTransicao(1, 0, 'b')
    af2.criaTransicao(2, 2, 'a')
    af2.criaTransicao(2, 4, 'b')
    af2.criaTransicao(3, 3, 'a')
    af2.criaTransicao(3, 3, 'b')
    af2.criaTransicao(4, 4, 'a')
    af2.criaTransicao(4, 4, 'b')

    print(Minimizacao.afEq(af1, af2))

    af3 = AFD('ab')
    for i in range(0, 4):
        af1.criaEstado(i)
    af1.mudaEstadoInicial(0)
    af1.mudaEstadoFinal(2, True)
    af1.criaTransicao(0, 1, 'a')
    af1.criaTransicao(0, 0, 'b')
    af1.criaTransicao(1, 2, 'a')
    af1.criaTransicao(1, 0, 'b')
    af1.criaTransicao(2, 2, 'a')
    af1.criaTransicao(2, 2, 'b')
    af1.criaTransicao(3, 3, 'a')
    af1.criaTransicao(3, 3, 'b')

    af4 = AFD('ab')
    for i in range(1, 5):
        af2.criaEstado(i)
    af2.mudaEstadoInicial(1)
    af2.mudaEstadoFinal(4, True)
    af2.criaTransicao(1, 1, 'a')
    af2.criaTransicao(1, 0, 'b')
    af2.criaTransicao(2, 2, 'a')
    af2.criaTransicao(2, 2, 'b')
    af2.criaTransicao(3, 3, 'a')
    af2.criaTransicao(3, 3, 'b')
    af2.criaTransicao(4, 4, 'a')
    af2.criaTransicao(4, 4, 'b')

    print(Minimizacao.afEq(af1, af2))
    
    print('***************************************************')
    
    af5 = AFD('ab')
    af5.criaEstado(1, True)
    af5.criaEstado(2, False, True)
    af5.criaTransicao(1,2,'b')
    af5.criaTransicao(2,1,'a')
    
    af6 = AFD('ab')
    af6.criaEstado(1, True)
    af6.criaEstado(2, False, True)
    af6.criaTransicao(1,2,'b')
    af6.criaTransicao(2,1,'b')
    
    print(Minimizacao.afEq(af5, af6))
    

