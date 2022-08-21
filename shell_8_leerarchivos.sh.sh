Ruta_path=$(pwd)
data="/rutas.txt"
ruta_completa="$Ruta_path$data"
declare -a array=()
n=0
for i in $(cat $ruta_completa); do
        ((n++))
        origen="$(cut -d';' -f1 <<<"$i")"
        array[$n]=$origen
done
echo ${array[3]}

