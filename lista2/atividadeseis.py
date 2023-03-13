numero = int(input("Digite um número inteiro: "))
fibonacci = [0, 1]

for i in range(2, numero):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
#append é acrecentar
print("A sequência de Fibonacci até o", numero, "º termo é:")
for i in range(numero):
    print(fibonacci[i], end=" ")