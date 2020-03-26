v=int(input('qual e o valor: '))
n100=0
n50=0
n10=0
n1=0
while v>0:
  if(v>=100):
    n100=n100+1
    v=v-100
  else:
    if(v>=50 and v<=99):
      n50=n50+1
      v=v-50
    else:
      if(v>=10 and v<=49):
        n10=n10+1
        v=v-10
      else:
        if(v>=1 and v<=9):
          n1=n1+1
          v=v-1


print('notas de 100:',n100)
print('notas de 50:',n50)
print('notas de 10:',n10)
print('notas de 1:',n1)
