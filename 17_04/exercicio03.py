x=int(input("Digite o valor de x"))
m=0
cont=0
while(x%2!=0):
  m=m+x
  cont=cont+1
  x=int(input("Digite o valor de x"))
if(m!=0 ):
  res=m/cont
  print("o resultado das media dos numeros impares foi: ",res)
else:
  print("voce nao digitou um valor impar")
