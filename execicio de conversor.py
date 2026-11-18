def cel_far (temp):
    far = temp * 1.8 + 32
    return far


def km_milhas (km):
    milhas = km * 0.6214
    return milhas
    
def kg_libras (kg):
     libras = kg * 2.2046
     return libras

def altura_area_base (altura, base):
     area = altura * base
     return area

def eh_primo (n):
     for i in range (2,n):
        if i % 1 == 0:
            return False
        return True
    

while True:
        print("================================================================")
        print("======== Escolha uma das opções abaixo ========")
        print("1- Conversor de temperatura de Celsius para Fahrenheit ")
        print("2- Conversor de distância de quilômetros para Milhas")
        print("3- Conversor de peso de quilogramas (kg) para libras")
        print("4- calcular área do retângulo")
        print("5- encontrar o maior número")
        print("6- Números primos")
        print("7- Sair")
        print("================================================================")        

        opção = input("Digite a opção desejada: ")

        
        if opção == "1":    
            temp = float(input("Digite a temperatura desejada em Celsius:"))
            far = cel_far(temp)
            print(f" A conversão de graus Celsius para Fahrenheit é de: {far:.2f}°F")
        
            
        if opção == "2":
                km = float(input("Diga a distância que deseja converter de KM para milhas: "))
                milhas = km_milhas(km)
                print(f" A conversão de distância de KM para Milhas é de: {milhas:.2f}")
                
        
        if opção =="3":
            kg = float(input("Digite o peso em quilogramas para converter em libras: "))
            libras = kg_libras(kg)
            print(f" A conversão de quilogramas para libras é de: {libras:.2f}")
            
        if opção =="4":
             altura = float(input("Digite a área do retângulo: "))
             base = float(input("Digite a base do retângulo: "))
             area = altura_area_base (altura, base)
             print(f" Um retângulo com a base igual a {base:.2f} e altura igual a {altura:.2f}, possuí uma área de {area:.2f} ")

        if opção == "5":
             num1 = int(input("Digite o primeiro número: "))
             num2 = int(input("Digite o segundo número: "))
             num3 =  int(input("Digite o terceiro número:"))
             if num1 > num2 and num1 > num3:
                  print(f"O maior número digitado foi {num1}")
             elif num2 > num3 and num2 > num1:
                  print(f"O maior número digitado foi {num2}") 
             elif num3 > num1 and num3 > num2:
                  print(f"O maior número digitado foi {num3}")

        if opção == "6":
                n = int(input("Digite o valor de N: "))
                i = eh_primo(n)
                print(f"O número digitado é: {i}")             

        if opção == "7":
            print("Muito Obrigado por utilizar este progama !")
            print("Progama Encerrando........")
            print("Progama Encerrado com sucesso!")
            break

        resp = input("Deseja continuar (s/n): ") 
        if resp == "s":
            continue
        else:
            break

