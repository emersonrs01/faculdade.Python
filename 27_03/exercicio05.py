i=0
r=0
while(i<5):
  x=int(input("qual e o valor de X: "))
  if(x%2==0):
    r=0
    for y in range(2,x):
      if(y%2!=0):
        r=r+y
    print("o somatorio dos valores pares foi: ",r)
  else:
    for i2 in range(1,11):
      r=i2*x
      print("tabuada do ",x,"*",i2,": ",r)
  i=i+1

