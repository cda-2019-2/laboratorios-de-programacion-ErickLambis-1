##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##

df10 = pd.read_csv("./q10=1/tbl2.tsv", sep="\t")
df10 = df10.sort_values(by=['_c5a'])
df10['_c5a'] = df10['_c5a'].apply(str) 
df10.head()
df10['comb'] = df10['_c5a'] + ":" + df10['_c5b'].map(str)
df10 = df10.groupby('_c0')['comb'].apply(list).reset_index(name='lista')
df10['lista'] = [','.join(map(str, l)) for l in df10['lista']]
df10.head()
