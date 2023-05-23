vetor1 = [1, 3, 5, 7, 9]
vetor2 = [2, 4, 6, 8, 10]
def merge_vetores(vetor1, vetor2):
    tamanho1 = len(vetor1)
    tamanho2 = len(vetor2)
    resultado = []
    i = 0 
    j = 0 

   
    while i < tamanho1 and j < tamanho2:
        if vetor1[i] < vetor2[j]:
            resultado.append(vetor1[i])
            i += 1
        else:
            resultado.append(vetor2[j])
            j += 1

    
    while i < tamanho1:
        resultado.append(vetor1[i])
        i += 1

   
    while j < tamanho2:
        resultado.append(vetor2[j])
        j += 1

    return resultado
    resultado = merge_vetores(vetor1, vetor2)
print(merge_vetores(vetor1, vetor2))