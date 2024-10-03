num = [0]*10
tam=len(num)
for x in range(tam):
    num[x] = int(input("entre com o numero: "))
saber = int(input("qual numero: "))
quantidade = 0
for i in range(tam):
    if saber == num[i]:
        quantidade+=1
print(quantidade)
