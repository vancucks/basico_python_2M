arrayNome = [0]*5
arraySenha = [0]*5
tam=len(arrayNome)

for i in range(tam):
    arrayNome[i] = input(f"digite o numero {i+1}: ")
    arraySenha[i] = input(f"digite a senha {i+1}: ")
for x in range(tam):
    print(f"login: {arrayNome[x]} | senha: {arraySenha[x]} posição: {x+1}")
