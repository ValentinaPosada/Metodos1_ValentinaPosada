factorial(){
  base=1
  n=$1
  while [ $n -gt 1 ];
  do
    base=$(( $base * $n ))
    n=$(( $n - 1 ))
  done
  echo $base
}

variacionessinrepeticion(){
  x=$(factorial $1)
  y=$(( $1 - $2))
  z=$(factorial $y)
  resultado=$(( $x / $z ))
  echo $resultado

}


variacionessinrepeticion 20 3
