##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el promedio de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    4.625000
##  B    5.142857
##  C    5.400000
##  D    3.833333
##  E    4.785714
##  Name: _c2, dtype: float64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
df2 = pd.read_csv("./q02=1/tbl0.tsv", sep="\t")
df2['_c2'].groupby(df2['_c1']).mean()
