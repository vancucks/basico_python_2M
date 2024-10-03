maior = 0
menor= 0
numero = [0]*5
tam = len(numero)
for i in range (tam):
    numero[i] = int(input("digite o numero: "))
for x in range(tam):
    if numero[x] %2 == 0:
        print(numero[x])
for y in range(tam):
    if numero[y] > maior:
        maior = numero[y]
print(f"esse é o maior: {maior}")
for q in range(tam):
    if numero[q] < menor:
        menor = numero[q]
print(f"esse é o menor: {menor}")
