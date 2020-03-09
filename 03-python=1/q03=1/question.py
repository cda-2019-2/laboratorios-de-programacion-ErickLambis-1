##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<
##
df=open('data.csv','r').readlines()
df=[row.split('\t') for row in df]
ext1=sorted(set([row[0] for row in df]))
ext2=sorted([[row[0],row[1]] for row in df])

for i in ext1:
 sumcol = 0
 for j in ext2:
   imp=j[0]
   if i == imp:
    sumcol = sumcol + int(j[1])
 print(i + ',' + str(sumcol))


