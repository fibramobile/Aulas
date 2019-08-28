# coding=utf-8
n1 = int(input("Digite sua quantidade de acoes: "))
n2 = int(input("Digite a proporcao do desdobramento(ex.: 1/8, digite apenas 8): "))
amountFuture = n2*n1
amountNow = amountFuture - n1
print ("A multiplicacao entre {} e {} é : {}" .format(n1, n2, amountNow))


