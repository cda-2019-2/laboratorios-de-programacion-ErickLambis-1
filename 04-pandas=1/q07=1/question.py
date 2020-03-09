##
##  Programación con Pandas
##  ===========================================================================
##
##  Agregue el año como una columna al archivo `tbl0.tsv`.
## 
##  Rta/
##      _c0 _c1  _c2         _c3   ano
##  0     0   E    1  1999-02-28  1999
##  1     1   A    2  1999-10-28  1999
##  ...
##  38   38   E    1  1999-09-28  1999
##  39   39   E    5  1998-01-26  1998
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

datos = pd.read_csv("tbl0.tsv",sep = '\t')


fecha = datos['_c3']
m=[row.split('-') for row in fecha]
new_datos = datos.assign(ano=[row[0] for row in m])
print(new_datos)
