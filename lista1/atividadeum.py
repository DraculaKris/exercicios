while True:
    num1 = float(input("insire um número:"))
    num2 = float(input("insire outro número:"))


    print("Escolha sua operação- 1-Soma, 2-subtração, 3-multiplicação, 4- divisão, 5- potenciação")
    escolha = int(input("insire sua operação desejada:"))

    def subtracao (a,b):
        return a - b

    def multiplicacao (a,b):
        return a * b

    def divisao (a,b):
        return a / b

    def soma (a,b):
        return a + b

    def potenciacao (a,b):
        return a ** b

    if escolha == 1: 
        print("A soma é " + str(soma(num1, num2)))
        print ("É válido")
    
    elif escolha == 2:
        print("A subtração é " + str(subtracao(num1, num2)))
        print ("É válido")
     
    elif escolha == 3:
        print("A multiplicação é " + str(multiplicacao(num1, num2)))
        print ("É válido")
    
    elif escolha == 4:
        print("A divisão é " + str(divisao(num1, num2)))
        print ("É válido")
    
    elif escolha == 5:
        print("A potenciação é " + str(potenciacao(num1, num2)))
        print ("É inválido" )
        
    resposta = int (input("Deseja realizar de novo?\n 1 - sim \n 2 - não \n"))
    
    if resposta == 2:
        break
