##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
##

m=open('data.csv','r').readlines()
m=[row.replace('\n','') for row in m]
m=[row.split('\t') for row in m]

l=[[row[0],row[4].split(',')]  for row in m]

lista=[]

for i in l:
  sumcol=0
  for j in i[1]:
   j= j.split(':')
   letra=i[0]
   sumcol = sumcol + int(j[1])
  print(letra,str(sumcol),sep=',')

