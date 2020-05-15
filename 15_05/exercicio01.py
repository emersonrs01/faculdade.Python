def principal(x,y):
  cont=0
  while(x<0 or x>100):
    x=int(input("digite o valor de x sendo de 0 a 100: "))
  while(y<0 or x>100):
    y=int(input("digite o valor de y sendo de 0 a 100:"))
  if(y<x):
    z=x
    x=y
    y=z
  for x in range(x,y):
    if(x%2==0):
      cont=cont+x
      print(x)
  return(cont)

x=int(input("digite o valor de x: "))
y=int(input("digite o valor de y: "))  
res=principal(x,y)
print("o valor da soma foi",res)
