function help(){
	echo Debe ingresar tres parametros 
}

if [ $# -eq 3 ]; then
	echo Corriendo pograma
else 
	help 
	exit 1 
fi 
