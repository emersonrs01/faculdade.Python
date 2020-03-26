total=0
for i in range(1,51):
 nt1=float(input('Prova 1: '))
 nt2=float(input('Prova 2: '))
 m=(nt1+nt2)/2
 if(m<7.0 and m>=3):
   total=total+1
 print('o aluno ',i,' ficou com media: ',m)
print('A quantidade de alunos em exame: ' ,total) 