a=int(input("Qual e o valor de A: "))
if(a<0):
  print("o numero nao pode ser negativo")
calc=0

b=-1
while(b<a):
  b=int(input("qual e o valor de B: "))
for i in range(a,b):
  if(i%2==0):
    calc=calc+i

print("a soma dos numero pares foi: ",calc)