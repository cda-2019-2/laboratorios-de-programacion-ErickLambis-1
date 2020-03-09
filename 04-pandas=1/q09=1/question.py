##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##

df9 = pd.read_csv("./q09=1/tbl1.tsv", sep="\t")
df9 = df9.sort_values(by=['_c4'])
df9['_c4'] = df9['_c4'].apply(str) 
df9 = df9.groupby('_c0')['_c4'].apply(list).reset_index(name='lista')
df9['lista'] = [','.join(map(str, l)) for l in df9['lista']]
df9.head()
