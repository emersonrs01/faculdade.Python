x=int(input("digite o valor de X: "))
y=int(input("digite o valor de y: "))
for i in range(x,y):
  if(i%3==0):
    for j in range(1,11):
      res=i*j
      print("tabuada do",i,":" ,i,"*" ,j,":",res)
