x=(input("digite o valor de A: "))
y=-1
while(x>y):
  y=int(input("digite o valor de B: "))
for i in range(x,y+1):
  for x in range(1,11):
    r2=i*x
    print(i,"*",x,": ",r2)