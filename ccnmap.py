import nmap

nmap = nmap.PortScanner()

def portScan():
    host = input("Please enter the IP address you would like to port scan - ")
    nmap.scan(host, '21 -1000')
    print(nmap.command_line())
    
    for host in nmap.all_hosts():
        print('')
        print('Host : %s (%s)' % (host, nmap[host].hostname()))
        print('State : %s' % nmap[host].state())

    for protocol in nmap[host].all_protocols():
        print('')
        print('Protocol : %s' % protocol)

        portList = nmap[host][protocol].keys()
        for port in portList:
            print("port : %s\tstate : %s" % (port, nmap[host][protocol][port]["state"]))