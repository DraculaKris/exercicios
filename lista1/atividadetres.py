numero= int(input("Informe um número:"))
division = numero - 1
primo = True

while division > 1:
    if(numero % division == 0):
        print(" Não é primo")
        primo = False
        break
    
    division = division -1
    7

if primo:
    print ("É primo")