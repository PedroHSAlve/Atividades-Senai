while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print(f"O número digitado {num} é par.") 
    else: 
        print(f"O número digitado {num} é ímpar.")
    
    resp = input("Deseja continuar? (s/n): ")
        
    if resp == "s":
            continue
    else:
        print("Programa encerrado.")
        print("Obrigado por utilizar o programa.")  
        break    