import os


def get_net_ip():
    ips = os.popen("ipconfig").read()
    ips = ips.split('\n')
    for ip in ips:
        if "IPv4" in ip:
            final_ip = ip.split(':')
            final_ip = final_ip[1]
            network_ip = final_ip
            break

    print(f"the network ip is {network_ip}")
    return network_ip

def get_range_from_ip(ip):
    pieces = ip.split('.')
    for piece in pieces:
        piece = piece.strip()
        print(f"#{piece}#")
    netrange = f"{pieces[0].strip()}.{pieces[1].strip()}"
    offline_ips = []
    online_ips = []
    print(f"the netrange is: {netrange}")
    #for i in range (255):
    for j in range(255):
        addr = f"{netrange}.0.{j}"
        output = os.popen(f"ping {addr} -n 1").read()
        if "TTL" in output:
            online_ips.append(addr)
        else:
            offline_ips.append((addr))

    print(f"Online Ips: {online_ips}")
    print(f"Offline IPs: {offline_ips}")



if __name__ == "__main__":
    ip = get_net_ip()
    get_range_from_ip(ip)
