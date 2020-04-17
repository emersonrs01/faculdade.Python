a=int(input("Qual e o valor de A: "))
b=int(input("qual e o valor de B: "))
calc=0

for i in range(a,b+1):
  if(i%2!=0):
    calc=calc+i

print("o valor das somas dos numeros impares foi: ",calc)