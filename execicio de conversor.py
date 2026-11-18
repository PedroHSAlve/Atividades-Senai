

def km_milhas (km):
    milhas = km * 0.6214
    return milhas
    

def cel_far (temp):
    far = temp * 1.8 + 32
    return far

def kg_libras (kg):
     libras = kg * 2.2046
     return libras

while True:
        print("================================================================")
        print("======== Escolha uma das opções abaixo ========")
        print("1- Conversor de temperatura de Celsius para Fahrenheit ")
        print("2- Conversor de distância de quilômetros para Milhas")
        print("3- Conversor de peso de quilogramas (kg) para libras")
        print("4- Sair")
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
            
        
        if opção == "4":
            print("Muito Obrigado por utilizar este progama !")
            print("Progama Encerrando........")
            print("Progama Encerrado com sucesso!")
            break

        resp = input("Deseja continuar (s/n): ") 
        if resp == "s":
            continue
        else:
            break

