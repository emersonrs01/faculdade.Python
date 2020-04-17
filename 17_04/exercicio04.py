y=int(input("digite o valor de y: "))
cont=0
for i  in range (1,y+1):
  if(y%i==0):
    cont=cont+1

if(cont==2):
  print(y,"e primo")
else:
  print(y,"nao e primo")
