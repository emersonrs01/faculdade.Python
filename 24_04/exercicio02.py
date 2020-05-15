y=90
cont=0
x=0
while(y>89):
  for i  in range (1,y+1):
    if(y%i==0):
      cont=cont+1

  if(cont==2):
    x=x+1
    print(y,"e primo")
  else:
    print(y,"nao e primo")
  y=y+1
