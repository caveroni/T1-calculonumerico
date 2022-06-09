
#Nome: Maria Verônica Pêgo de Souza
#Matrícula: 2112470GPRO
#TRABALHO COMPUTACIONAL 1 (T1) DE CÁLCULO NUMÉRICO EP – 2022-1 (4.0 pt)


e = float(input("precisão: ")) #1

def fdex(x):
        fx=((1/48)*(693*(x**6)-945*(x**4)+315*(x**2)-15))
        return fx

periodo=[]
for i in range(-10,10): # (Todos os zeros dos polinômios de Legendre são menores do que 1(um) em módulo e são simétricos em relação a origem.)

    if fdex((0.1)*i)*fdex(0.1*(i+1))<0: #2
        periodo.append([round(0.1*i,5),round(0.1*(i+1),5)])

for n in range(len(periodo)):

    print("\n X", n+1)
    print("● intervalo (a, b) que contém a raiz:", periodo[n])
    j=periodo[n][0]
    k=periodo[n][1]
    i=0

    if k-j<e:
        i+=1
        x=(j+k)/2
        print("● Aproximação pelo método da Bissecção:", x)
        print("● Número de iterações pelo método da Bissecção:", i)


    else:
        while True:
            i+=1
            x=(j+k)/2 
            fxum=fdex(j)
            fxdois=fdex(k)
            fx=fdex(x)
            if fx==0.0:
                print("● Aproximação pelo método da Bissecção:",x)
                print("● Número de iterações pelo método da Bissecção", i)
                break

            elif fxum*fx<0: 
                k=x
            elif fxum*fx>0:
                j=x


            if k-j<e:
                x = (j + k) / 2
                print("● Aproximação pelo método da Bissecção:", x)
                print("● Número de iterações pelo método da Bissecção:", i)
                break

    def Gx(x):
        Gx=(x-(1/48)*(693*(x**6)-945*(x**4)+315*(x**2)-15)/(1/8)/(693*(x**5)-630*(x**3)+105*x))
        return Gx

    i=0
    x0=(periodo[n][0]+ periodo[n][1])/2
    while True:
        i+=1
        x=Gx(x0)
        if abs(fdex(x)) < e or abs(x-x0)<e:

            break

        else:
            x0=x

    print("● Aproximação por Newton:", x)
    print("● Iterações pelo método de Newton:", i)