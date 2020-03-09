##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##


df=open('data.csv','r').readlines()
df=[row.split('\t') for row in df]
df=sorted([(row[0],row[1]) for row in df])
ext1=sorted(set([row[1] for row in df]))

for i in ext1:
 imp1 = []
 for j in df:
   num = j[1]
   if i == num:
    imp1.append(j[0])
 imp1=sorted(set(imp1))
 print((i,imp1))