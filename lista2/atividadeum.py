numero = int(input("Digite um número inteiro: "))

divisores = []

# Encontra todos os divisores do número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
        
print("Os divisores de", numero, "são:", divisores)
