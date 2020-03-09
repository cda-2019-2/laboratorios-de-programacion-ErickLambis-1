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

df4 = pd.read_csv("./q04=1/tbl1.tsv", sep="\t")
p4 = df4['_c4'].unique().tolist()
p4ord = sorted(p4, key = lambda v: v.upper())
[x.upper() for x in p4ord]

