from AFD import AFD

def acha(aux, n1, n2):
        for i in range(len(aux)):
            if(n1 == aux[i][0]) and (n2 == aux[i][1]):
                return i

class Operacoes:

    def inter(afd1, afd2, afd_res):
        len1 = len(afd1.estados)
        len2 = len(afd2.estados)
        aux = []
        finais1 = []
        finais2 = []
        fns = []
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                aux2 = []
                aux2.append(i)
                aux2.append(j)
                aux.append(aux2)

        for i in afd1.finais:
            finais1.append(i)
        for i in afd2.finais:
            finais2.append(i)

        for i in finais1:
            for j in finais2:
                k = []
                k.append(i)
                k.append(j)
                fns.append(k)

        for i in fns:
            s = acha(aux, i[0], i[1])
            s = s+1
            afd_res.mudaEstadoFinal(s, True)
        return afd_res
    
    def uni(afd1, afd2, afd_res):
        len1 = len(afd1.estados)
        len2 = len(afd2.estados)
        aux = []
        finais1 = []
        finais2 = []
        fns = []
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                aux2 = []
                aux2.append(i)
                aux2.append(j)
                aux.append(aux2)

        for i in afd1.finais:
            finais1.append(i)
        for i in afd2.finais:
            finais2.append(i)

        for i in range(len(aux)):
            if((aux[i][0] in finais1) or (aux[i][1] in finais1)) or ((aux[i][0] in finais2) or (aux[i][1] in finais2)):
                s = i + 1
                afd_res.mudaEstadoFinal(s, True)
                
        for i in fns:
            s = acha(aux, i[0], i[1])
            s = s+1
            afd_res.mudaEstadoFinal(s, True)
        return afd_res
    
    def dif(afd1, afd2, afd_res):
        afd1.mudaEstadoFinal(5, True)
        len1 = len(afd1.estados)
        len2 = len(afd2.estados)
        aux = []
        finais1 = []
        finais2 = []
        fns = []
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                aux2 = []
                aux2.append(i)
                aux2.append(j)
                aux.append(aux2)

        for i in afd1.finais:
            finais1.append(i)
        for i in afd2.finais:
            finais2.append(i)

        for i in finais1:
            for j in finais2:
                if(i in finais1) and not(i in finais2):
                    print("a")
                    k = []
                    k.append(i)
                    k.append(j)
                    fns.append(k)
        for i in fns:
            s = acha(aux, i[0], i[1])
            s = s+1
            afd_res.mudaEstadoFinal(s, True)
        print(afd_res)
        return afd_res