#ler x e y, calacular e mostrar a tabuada dos numeros inteiros entre x e y divisiveis por 3
#no final mostrar a tabuada dos numeros inteiros divisiveis por 3
x=int(input("variavel X: "))
y=int(input("variavel Y: "))
cont=0
for i in range(x+1,y):
    if(i%3==0):
        for j in range(1,11):
            tab=i*j
            print(f'tabuada do {i} multiplicado por {j} é {tab}')
        cont=cont+1
print(f'a quantidade de numeros divisiveis por 3 entre {x} e {y} são {cont}')