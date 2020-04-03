y=1
aux=0
total=0
while(y>0):
  y=int(input("digite o valor de y: "))
  if(y%2==0 and y!=0):
    aux=aux+1
    total=total+y
m=total/aux

print("a media foi ",m)

