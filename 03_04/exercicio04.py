a=(input("digite o valor de A: "))
b=0
while(a>b):
  b=int(input("digite o valor de B: "))
for i in range(a,b+1):
  if(i%2==0):
    for x in range(1,11):
      r2=i*x
      print(i,"*",x,": ",r2)