Archivos=$(ls *.csv)

for file in  ${Archivos[*]}
do
 letra=$(cut -c1 $file)
 
 for x in ${letra[*]} 
 do
  VAR1="${file},"
  VAR2=$x
  VAR3="$VAR1$VAR2"
  echo "$VAR3"
 done

done


