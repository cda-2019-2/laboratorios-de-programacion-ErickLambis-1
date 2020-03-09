##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
##

df=open('data.csv','r').readlines()
df=[row.replace('\n','') for row in df]
df=[row.split('\t') for row in df]
df=[row[4] for row in df]
df=[row.split(',') for row in df]
df=[j for row in df for j in row]
df=[row.split(':') for row in df]
ext1=sorted(set([row[0] for row in df]))

for i in ext1:
 conteo = 0
 for j in df:
   reg = j[0]
   if i == reg:
    conteo= conteo + 1
 print(i,conteo,sep=',')