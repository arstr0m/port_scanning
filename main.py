import nmap

scanner = nmap.PortScanner()
ip = input("IP: ")

try:
    scanner.scan(ip, "1-1024", "-v -sS ")
    print("Ip Status:", scanner[ip].state())
    scanner[ip].all_protocols()
    print("Found Ports:")
    for port in scanner[ip]['tcp'].keys():
        print(port, scanner[ip]['tcp'][port]['state'])
except nmap.PortScannerError as e:
    print("Error: ", e)
