##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
##

df=open('data.csv','r').readlines()
df=[row.split('\t') for row in df]
ext1=sorted(set([row[0] for row in df]))
ext2=sorted([[row[0],row[1]] for row in df])

for i in ext1:
 imp1 = []
 for j in ext2:
   imp2=j[0]
   if i == imp2:
    lista.append(j[1])
    
 print(i + ',' + max(imp1) + ',' + min(imp1))
