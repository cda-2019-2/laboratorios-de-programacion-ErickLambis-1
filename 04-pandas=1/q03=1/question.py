##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el maximo de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    9
##  B    9
##  C    9
##  D    7
##  E    9
##  Name: _c2, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
df3 = pd.read_csv("./q03=1/tbl0.tsv", sep="\t")
df2['_c2'].groupby(df2['_c1']).max()

