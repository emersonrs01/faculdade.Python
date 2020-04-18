r1=0
r2=0
for i in range(5):
  x=int(input("digite o valor de x: "))
  for i2 in range(2,x):
    r1=r1+i2
  if(r1>100):
    y=int(input("digite o valor de Y: "))
    z=x
    x=y
    y=z
  else:
    for i3 in range(1,11):
      r2=x*i3
      print(x,": ",i3,": ",r2)

