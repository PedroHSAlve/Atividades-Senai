def somar(a,b): return a + b 
def subtrair(a,b): return a - b
def multiplicação(a,b): return a * b
def divisão(a,b):
    if b == 0:return "Erro!"
    return a / b 

while True: 
    op = input("Operação (+-*/0):")
    if op == "0": break
    a = float(input("Núm1: "))
    b = float(input("Núm2: "))
    if op == "+": 
        print(somar(a,b))

    elif op == "-":
        print(subtrair(a,b))
    elif op == "*":
        print(multiplicação(a,b))
    elif op == "/":
        print(divisão(a,b))        
    
        