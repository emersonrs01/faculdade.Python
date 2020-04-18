n=input("digite o numero: ")
cont=1
soma=0

while (cont<n):
 if (n%cont==0):
    soma = soma + cont
    cont = cont + 1
 else:
    cont = cont + 1
     
     
if (soma==n):
  print("perfeito")
else:
  print("nao prefeito")