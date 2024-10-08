def imprime_nome(nome):
    print(f"Nome:{nome}")
def imprime_numero(n):
    for x in range(1,n+1,1):
        print(x)

def somar(num1,num2,num3,num4,num5):
    somar= num1+num2+num3+num4+num5
    print(somar)

def soma (*numeros):
    print(numeros)

def somar_arg(*numeros):
    soma=0
    for i in numeros:
        soma+=i
    print(soma)

def contador_texto(*texto):
    cont= 0
    for i in texto[0]:
        if i not in " !@#$%&*":
            cont +=1
    print(cont)
    tam = len(texto[0])
    for x in range(tam-1,-1,-1):
        print(texto[0][x],end="")
    print(texto[0][::-1])
def numeros_iguais(novos, numeros):
    print(numeros)
    for x in numeros:
        if x not in novos:
            novos.append(x)
    print(novos)

def numero_primo (n):
    if n == 1:
        return n, "numero não primo"
    elif n == 2:
        return n, "ele é primo"
    else:
        for x in range(2,n):
            if (n % x==0):
                return n, "numero não primo"

        return n, "ele é primo"



