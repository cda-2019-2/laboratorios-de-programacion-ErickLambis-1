##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
##

import pandas as pd
df4=pd.read_csv('tbl1.tsv', sep='\t')
p4=df4['_c4'].str.upper()
p4=sorted(p4.unique())
print(p4)

