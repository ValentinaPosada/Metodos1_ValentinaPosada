pass=0

checkvalue() {
  pass=1
  exit 1
}

while [ $pass -eq 0 ];
do
  while read -r parametro1;
  do
      if [ $parametro1 -eq 0 ] || [ $parametro1 -eq 1 ];then
        checkvalue
      else
        echo "intentelo de nuevo"
      fi
  done
done

 
  










