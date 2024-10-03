arrayNum = [0]*5
tam=len(arrayNum)
for i in range(tam):
    arrayNum[i] = int(input(f"digite o numero {i+1}: "))
for x in range(tam-1,-1,-1):
    print(arrayNum[x], end=" ")