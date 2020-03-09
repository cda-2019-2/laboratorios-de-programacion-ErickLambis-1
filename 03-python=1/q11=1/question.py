##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
##

df=open('data.csv','r').readlines()
df=[row.split('\t') for row in df]

l=[[row[1],row[3].split(',')]  for row in df]

ext1=[]

for i in l:
  for j in i[1]:
    x=i[0],j[0]
    ext1.append(x)

ext2=sorted(set([row[1] for row in ext1]))

for i in ext2:
 sumcol = 0
 for j in ext1:
   ext2=j[1]
   if i == ext2:
    sumcol = sumcol + int(j[0])
    
 print(i,str(sumcol),sep=',')
