m2=0
aux=0
for i in range(1,4):
  print("notas do aluno: ",i)
  n1=float(input("Qual a primeira nota: "))
  n2=float(input("qual a segunda no: "))
  m1=(n1+n2)/2

  if(m1<3):
    aux=aux+1
    m2=m2+m1
if(aux==0):
  print("nao teve alunos reprovados")
else:
  t=m2/aux
  print(aux," Aluno reprovaram com media de: ",t)

