#!/bin/bash
# colocar wget para fazer progresso de um download

inicio='[.................................................]  0%'
passo='#####'
echo -n $inicio 
for i in 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100; do
	sleep 0.2
	pos=$((i/2-5))
	echo -ne '\033[G'
	echo -ne "\033[${pos}C"
	echo -n "$passo"
	echo -ne '\033[53G'
	echo -n "$i%"
done
echo
