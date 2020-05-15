y=90
x=0
while(x<3):
  cont=0
  for i  in range (1,y+1):
   if(y%i==0):
     cont=cont+1

  if(cont==2):
   print(y,"e primo")
   x=x+1
  y=y+1
