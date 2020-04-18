for i in range(5):
  w=int(input("digite o valor de W: "))
  if(w%2==0):
    for j in range(1,w+1):
      r=w*j
      print(j,": ",j,": ",r)
  else:
    f=1
    for x in range(1,w+1):
      f=f*x
    print("fatorial: ",f)
  