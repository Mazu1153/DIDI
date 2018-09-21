
n1= int(input("digite um numero: "))
n2= int(input("digite um valor: "))
n3= int(input("digite um valor: "))

if n1 > n2 > n3:
    print("o maior valor", n1, "e o menor valor", n3)
if n1 > n3 > n2:
    print("o maior valor", n1, "e o menor valor", n2)
if n2 > n1 > n3:
    print("o maior valor", n2, "e o menor valor", n3)
if n2 > n3> n1:
    print("o maior valor", n2, "e o menor valor", n1)
if n3 > n1 > n2:
    print("o maior valor", n3,  "e o menor valor", n2)
if n3 > n2 > n1:
    print("o maior valor", n3,"e o menor valor", n1)
