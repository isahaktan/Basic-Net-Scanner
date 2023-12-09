import scapy.all as scapy
import optparse



def user_input_ip():
    ip_obj = optparse.OptionParser()
    ip_obj.add_option("-i","--ipaddress",dest="ip_address",help="---")
    (user_input_arg,arguments) = ip_obj.parse_args()
    return user_input_arg

def scanner(ip):

    arp_rq = scapy.ARP(pdst=ip)
    broadcast_rq = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #vur tum ağa dağılsın
    combine = broadcast_rq/arp_rq #iki paketi birleştirdim.
    (accept_list,unaccept_list) = scapy.srp(combine,timeout=1) #paketi olusturdun ve bu paketi göndermen lazım.
    accept_list.summary() #ozet

user_ip_address = user_input_ip()
scanner(user_ip_address.ip_address)
