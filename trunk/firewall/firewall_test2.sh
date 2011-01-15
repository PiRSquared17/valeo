#!/bin/bash
# Execute: "# chmod +x /etc/init.d/firewall_test2"
# firewall_test2 [start, stop, restart]

iniciar(){

# Abre para uma faixa de endereços da rede local
iptables -A INPUT -s 192.168.0.0/255.255.255.0 -j ACCEPT

# Abre uma porta (inclusive para a internet)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Ignora pings
iptables -A OUTPUT -p icmp --icmp-type echo-request -j DROP

# Protege contra IP spoofing
echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter

# Evita que o firewall repasse pacotes potencialmente prejudiciais aos 
# micros da rede interna
iptables -A FORWARD -m unclean -j DROP

# Abre para a interface de loopback.
iptables -A INPUT -i lo -j ACCEPT

# Impede a abertura de novas conexões, efetivamente bloqueando o acesso 
# externo ao seu servidor, com exceção das portas e faixas de endereços 
# manualmente especificadas anteriormente. Bloqueia tudo.
iptables -A INPUT -p tcp --syn -j DROP
}

parar(){
iptables -F
echo "Regras de firewall desativadas"
}
case "$1" in 
"start") iniciar ;; 
"stop") parar ;; 
"restart") parar; iniciar ;;
*) echo "Use os parâmetros start ou stop"
esac
