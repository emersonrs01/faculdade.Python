z=int(input("qual e o valor de z: "))
r=0

for x in range(1,z):
  if(x%2==0):
    r=r+x

print("numero pares do laco: ",r)