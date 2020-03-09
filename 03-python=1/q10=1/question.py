##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##

df=open('data.csv','r').readlines()
df=[row.replace('\n','') for row in df]
df=[row.split('\t') for row in df]

reg=[[row[0],row[3],row[4]] for row in df]

for i in reg:
    a=i[0]
    b=len(i[1].split(','))
    c=len(i[2].split(','))
    print(a,b,c,sep=',')