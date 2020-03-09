##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
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
c=sorted(set([row[0] for row in df]))

for i in c:
 imp1 = []
 for j in df:
   imp2=j[0]
   if i == imp2:
    lista.append(j[1])
    mx=max(imp1)
    mn=min(imp1)
    
 print(i + ',' + mn + ',' + mx)