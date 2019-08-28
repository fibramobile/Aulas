n1 = int(input("Entre com numero 1: "))
n2 = int(input("Entre com numero 2: "))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2

print("A soma é {}\nA multiplicacao é {}\nA divisao é {}\n".format(soma,mult,div) , end = "")
print("A divisao inteira é {} e a Exponenciacao é {}|".format(divInt, exp))
