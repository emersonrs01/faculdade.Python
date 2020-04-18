k=-1
r=0
while(k!=0):
  k=int(input("Digite o valor de k: "))
  if(k>0):
    for i in range(2,k):
      if(i%2!=0):
        r=r+i
    print("o somatorio dos valores impares foi: ",r)
    r=0
  if(k<0):
    print("k nao pode ser menor de 0")


