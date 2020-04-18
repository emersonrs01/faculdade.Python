cont=0
for i in range(5):
  x=int(input("Digite o valor de x: "))
  if(x%2==0):
    for t in range(2,x):
      if(t%2!=0):
        cont=cont+t
    print("o somatorio dos valores impares foi: ",cont)
  else:
    for j in range(1,11):
      r=x*j
      print(x,"*",j,":",r)
