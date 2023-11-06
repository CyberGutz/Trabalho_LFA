class Minimizacao:
    def __init__(self):
        from Trabalho1.AFD import AFD

    @staticmethod
    def __transicoes(afd):
        transicoes = []
        for i in afd.estados:
            for j in afd.alfabeto:
                if (i, j) in afd.transicoes.keys():
                    transicoes.append([i, afd.transicoes.get((i, j)), j])
        return transicoes

    @staticmethod
    def stateEq(afd, id1, id2):
        # Casos Triviais: 1- Se um dos dois estados não estiver no afd.
        if id1 not in afd.estados or id2 not in afd.estados:
            return False
        # 2- Se um dos estados for final, e o outro não.
        elif (id1 in afd.finais and id2 not in afd.finais) or (id2 in afd.finais and id1 not in afd.finais):
            return False
        # 3- Se ambos estados sâo iguais.
        elif id1 == id2:
            return True
        # Verificação de transições: itera o alfabeto
        for i in afd.alfabeto:
            # Se um dos estados tiver transição com aquele caractere do alfabeto e o outro não,
            # os estados são diferentes.
            # Se as transições forem iguais e o algoritmo já testou todo o alfabeto.
            if ((id1, i) in afd.transicoes.keys()) != ((id1, i) in afd.transicoes.keys()):
                return False
            if afd.transicoes.get((id1, i)) == afd.transicoes.get((id2, i)) and i == afd.alfabeto[
            len(afd.alfabeto) - 1]:
                return True
            if afd.transicoes.get((id1, i)) == id2 and afd.transicoes.get((id2, i)) == id1:
                pass
            # Caso contrário, testa as transições seguintes, até terminar o alfabeto inteiro.
            elif afd.transicoes.get((id1, i)) is not None or afd.transicoes.get((id2, i)) is not None:
                if Minimizacao.stateEq(afd, afd.transicoes.get((id1, i)), afd.transicoes.get((id2, i))):
                    pass
                else:
                    return False
        # Se o algoritmo não verificou nenhuma diferença entre os estados, então eles são iguais.
        return True

    @staticmethod
    def estadosEquivalentes(afd):
        equivalentes = []
        for i in afd.estados:
            aux = []
            for j in afd.estados:
                if [i, j] in equivalentes or [j, i] in equivalentes:
                    continue
                if Minimizacao.stateEq(afd, i, j) and i != j:
                    aux.append(i)
                    aux.append(j)
                if not aux or aux in equivalentes:
                    continue
                equivalentes.append(aux)
        return equivalentes

    @staticmethod
    def concatAF(afd1, afd2):
        for i in afd2.estados:
            afd1.criaEstado(int("1{}".format(i)))
            for j in afd1.alfabeto:
                if (i, j) in afd2.transicoes:
                    afd1.criaTransicao(int("1{}".format(i)), "1{}".format(afd2.transicoes.get((i, j))), j)
            if i in afd2.finais:
                afd1.mudaEstadoFinal("1{}".format(i), True)
        return afd1

    @staticmethod
    def afEq(afd1, afd2):
        afConcatenado = Minimizacao.concatAF(afd1, afd2)
        if Minimizacao.stateEq(afConcatenado, afd1.inicial, int("1{}".format(afd2.inicial))):
            return True
        else:
            return False

    @staticmethod
    def minimizacao(afd):
        equivalentes = Minimizacao.estadosEquivalentes(afd)
        for i in equivalentes:
            for j in afd.estados:
                for k in afd.alfabeto:
                    if (j, k) in afd.transicoes:
                        if afd.transicoes[(j, k)] == i[1] and j != i[1]:
                            del afd.transicoes[(j, k)]
                            afd.criaTransicao(j, i[0], k)
                        if j == i[1]:
                            del afd.transicoes[(j, k)]
            afd.estados.remove(i[1])
