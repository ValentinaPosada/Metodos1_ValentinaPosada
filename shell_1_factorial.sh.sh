n=$1
parametro=1

if [ $# -eq 0 ]; then
	echo Tiene que ingresar un parametro

elif [ $n -eq 0 ] || [ $n -eq 1 ]; then 
	echo El factorial de $n es $parametro

else
	while [ $n -gt 1 ]
	do 
		let parametro=$parametro*$n
		let n=$n-1
	done 
	echo El factorial de $1 es $parametro

fi



