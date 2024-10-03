nome = [0]*5
tamanho= len(nome)
for x in range (tamanho):
    nome[x]= input("digite o nome: ")
for i in range (tamanho):
    print(i+1, nome[i])
for c in range (tamanho-1,-1,-1):
    print(c+1, nome[c])