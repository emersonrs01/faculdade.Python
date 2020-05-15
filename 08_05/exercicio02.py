def somatorio(v):
  r=0
  for i in range(1,v):
    r=r+i
  return(r)
  
a=int(input("digite o valor de A: "))
b=int(input("digite o valor de b: "))
if(a%2==0 and b%2==0):
  res=somatorio(a)
else:
  if(b%2==0):
    res=somatorio(b)
  else:
    res=somatorio(a+b) 
print(res)
