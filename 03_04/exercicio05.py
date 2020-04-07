r=0
for i in range (5):
  x=int(input("qual o valor de x: "))
  f=1
  for i2 in range(1,x+1):
    f=f*i2
  if(f<=100):
    for i3 in range (1,f+1):
      r=x*i3
      print(i3,": ",x,": ",r)
  else:
    r=0
    for i4 in range (2,x):
      r=r+i4
    print("o somatorio dos numero foi: ",r)
