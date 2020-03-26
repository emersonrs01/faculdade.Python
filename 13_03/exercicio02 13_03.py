a=float(input('qual e o valor de A: '))
b=float(input('qual e o valor de B: '))
c=float(input('qual e o valor de C: '))
r1=0
r2=0
r3=0

if(a>b and a>c):
  if(b>c):
    r1=a
    r2=b
    r3=c
  else:
    r1=a
    r2=c
    r3=b

if(b>a and b>c):
  if(a>c):
    r1=b
    r2=a
    r3=c
  else:
    r1=b
    r2=c
    r3=a

if(c>a and c>b):
  if(a>b):
    r1=c
    r2=a
    r3=b
  else:
    r1=c
    r2=b
    r3=a

print('o maior valor e: ',r1)
print('o segunro maior valor e: ',r2)
print('o terceiro maior valor e: ',r3)