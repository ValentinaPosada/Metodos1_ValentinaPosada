
Ruta_path=$(pwd)
data="/data"
ruta_completa="$Ruta_path$data"

if [ ! -f  $ruta_completa ];then
        echo $ruta_completa
        mkdir $ruta_completa
        exit
fi
~

