#!/bin/sh

# Inicialização:
# Debian: "/etc/init.d/bootmisc.sh"
# Red Hat: "/etc/rc.d/rc.local"

# Testes com nmap:
# nmap -sS -v 192.168.0.33
# nmap -P0 -v 192.168.0.33

#Internet=eth1
#Rede Interna=eth0
echo "Iniciando Firewall...................................[ OK ]"

echo " Carregando Banco de dados ..........................[ OK ]"
# Ativa modulos
modprobe ip_tables
modprobe iptable_nat
modprobe ip_conntrack
modprobe ip_conntrack_ftp
modprobe ip_nat_ftp
modprobe ipt_REJECT
modprobe ipt_MASQUERADE
modprobe ipt_MARK
modprobe ipt_mark
modprobe ipt_mac
modprobe ipt_tos
modprobe iptable_mangle
modprobe iptable_filter
echo " Carregando Modulos .................................[ OK ]"

# Zera regras
iptables -F
iptables -X
iptables -F -t nat
iptables -X -t nat
iptables -F -t mangle
iptables -X -t mangle
iptables -F -t filter
iptables -X -t filter
echo " Limpando as Regras .................................[ OK ]"

# Bloqueia o acesso à web de IPs específicos
ip1="192.168.0.67"
ip2="192.168.0.43"
iptables -A FORWARD -p tcp -s $ip1 -j REJECT
iptables -A FORWARD -p tcp -s $ip2 -j REJECT
echo "Bloqueando IPs: $ip1 $ip2 .......................[ OK ]"

# Determina a politica padrao
iptables -P INPUT DROP
iptables -P FORWARD DROP
echo " Alterando a politica padrao ........................[ OK ]"

# Aceita os pacotes que realmente devem entrar
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Protege contra ICMP Broadcasting
echo "1" > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts
echo "Ativando a controle de Broadcasting .................[ OK ]"

# Protege contra synflood
echo "1" > /proc/sys/net/ipv4/tcp_syncookies
echo "Ativando controle de synflood .......................[ OK ]"

# A tentativa de acesso externo a estes servicos serao registrados no syslog
# do sistema e serao bloqueados pela última regra abaixo
iptables -A INPUT -i eth1 -p tcp --dport 21 -j LOG --log-prefix "FIREWALL: ftp "
iptables -A INPUT -i eth1 -p tcp --dport 21 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 22 -j LOG --log-prefix "FIREWALL: ssh "
iptables -A INPUT -i eth1 -p tcp --dport 22 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 25 -j LOG --log-prefix "FIREWALL: smtp "
iptables -A INPUT -i eth1 -p tcp --dport 25 -j DROP
iptables -A INPUT -i eth1 -p udp --dport 53 -j LOG --log-prefix "FIREWALL: dns "
iptables -A INPUT -i eth1 -p udp --dport 53 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 110 -j LOG --log-prefix "FIREWALL: pop3 "
iptables -A INPUT -i eth1 -p tcp --dport 110 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 113 -j LOG --log-prefix "FIREWALL: identd "
iptables -A INPUT -i eth1 -p tcp --dport 113 -j DROP
iptables -A INPUT -i eth1 -p udp --dport 111 -j LOG --log-prefix "FIREWALL: rpc"
iptables -A INPUT -i eth1 -p udp --dport 111 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 111 -j LOG --log-prefix "FIREWALL: rpc"
iptables -A INPUT -i eth1 -p tcp --dport 111 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 137:139 -j LOG --log-prefix "FIREWALL: samba "
iptables -A INPUT -i eth1 -p tcp --dport 137:139 -j DROP
iptables -A INPUT -i eth1 -p udp --dport 137:139 -j LOG --log-prefix "FIREWALL: samba "
iptables -A INPUT -i eth1 -p udp --dport 137:139 -j DROP
iptables -A INPUT -i eth1 -p tcp --dport 2210 -j LOG --log-prefix "FIREWALL: ssh_leo "
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s -j LOG --log-prefix "FIREWALL: Ping Input "
iptables -A FORWARD -p icmp --icmp-type echo-request -m limit --limit 1/s -j LOG --log-prefix "FIREWALL: Ping Forward "

# Bloqueando MSN, por porta ou acesso via web
iptables -A OUTPUT -p tcp --dport 1863 -j REJECT
iptables -A FORWARD -p tcp --dport 1863 -j REJECT
iptables -A OUTPUT -d messenger.hotmail.com -j DROP
iptables -A FORWARD -d messenger.hotmail.com -j DROP
iptables -A OUTPUT -d webmessenger.msn.com -j DROP
iptables -A FORWARD -d webmessenger.msn.com -j DROP
iptables -A OUTPUT -d meebo.com -j DROP
iptables -A FORWARD -d meebo.com -j DROP
echo "Bloqueando MSN  .................................[ OK ]"

#rede liberada
iptables -t filter -A FORWARD -d 0/0 -s 192.168.0.10 -j ACCEPT
iptables -t filter -A FORWARD -d 192.168.0.10 -s 0/0 -j ACCEPT
iptables -t filter -A INPUT -s 192.168.0.10 -d 0/0  -j ACCEPT
iptables -t nat -A POSTROUTING -s 192.168.0.10 -o eth1 -j MASQUERADE
echo "Ativando controle de logs ...........................[ OK ]"

#Pacote marcado
iptables -A PREROUTING -t mangle -i eth0 -s $IPSOURCE -j MARK --set-mark $CBQMARK

#Compartilha a conexao
echo 1 > /proc/sys/net/ipv4/ip_forward

# Proxy transparente
iptables -t nat -A PREROUTING -i eth0 -p tcp -d ! 200.201.0.0/16 --dport 80 -j REDIRECT --to-port 3128

#SSH
iptables -A INPUT -p tcp --dport 2210 --syn -j ACCEPT
iptables -A INPUT -p tcp --dport 80 --syn -j ACCEPT

#Redirecionamento de portas
iptables -A INPUT -p tcp --dport 22 --syn -j ACCEPT
iptables -A INPUT -p tcp --dport 5912 --syn -j ACCEPT
iptables -A INPUT -p tcp --dport 5909 --syn -j ACCEPT

# Liberando acesso pelo IP e MAC da placa: "arp -a" ou "ifconfig"
iptables -A INPUT -s 192.168.1.100 -m mac --mac-source 00:11:D8:76:59:2E -j ACCEPT

iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 22 -j DNAT --to 172.168.0.10
iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 5912 -j DNAT --to 192.168.0.12
iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 5909 -j DNAT --to 192.168.0.9

#Rota ip fixo clientes
iptables -t nat -A PREROUTING -d 200.101.67.134 -j DNAT --to 172.168.0.3

#Fecha o resto
iptables -A INPUT -j DROP
iptables -A FORWARD -j DROP
echo "Iniciando Firewall...................................[ OK ]"
