##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  >>> Escriba su codigo a partir de este punto <<<
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]

sumcol = 0

for i in data:
  sumcol = sumcol + int(i[1])
print(sumcol)
