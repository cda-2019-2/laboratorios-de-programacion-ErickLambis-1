##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
df11_1 = pd.read_csv("./q11=1/tbl2.tsv", sep="\t")
df11_2 = pd.read_csv("./q11=1/tbl0.tsv", sep="\t")
print(df11_1.columns, '\t', df11_2.columns)
df11_join = df11_1.merge(df11_2, left_on = '_c0', right_on = '_c0', how='right').copy()
df11_join = df11_join.groupby('_c1')['_c5b'].apply(sum).reset_index(name='lista')
df11_join


