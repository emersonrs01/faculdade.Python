x=1
r=0
acum=0
f=0
while(x!=0):
  x=int(input("digite o valor de x: "))
  if(x<0):
    print("o valor nao pode ser negativo")
  for i in range (1,x+1):
    f=f*i
    r=r+f
  acum=acum+1 
r2=r/acum
print("a media dos fatorias foi: ",r2)