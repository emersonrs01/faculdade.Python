x=0
while(x<5):
  z=int(input("qual o valor de z: "))
  if(z%2==0):
    for i in range(1,11):
      r=z*i
      print("tabuada do ",z," : ",r)
  else:
    f=1
    for i in range(1,z+1):
      f=f*i
    print("fatorial: ",f)
  x=x+1