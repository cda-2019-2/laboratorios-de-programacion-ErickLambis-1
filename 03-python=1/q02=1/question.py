##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  >>> Escriba su codigo a partir de este punto <<<
##
df1=open('data.csv','r').readlines()
df1=[row.split('\t') for row in df1]
df1=[row[0] for row in df1]
df1=sorted(df1)

df2={}
 
for j in df1:
    if j in df2:
        df2[j]=df2[j]+1
    else:
        df2[j]=1

for i in df2:
    print(i + ',' + str(df2[i]))