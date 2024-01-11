import nmap

scanner = nmap.PortScanner()

print('Jeff Scanner')
print('----------------------')

ip = input('Digite o IP: ')
print('O ip digitado foi ', ip)
type(ip)

menu = input('''\n Escolha o tipo de varredura
    1 - Syn
    2 - UDT
    3 - intensa
''')

print('Escolha uma opção', menu)

if menu == '1':
    print('Versão do nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('Status do ip: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas abertas: ', scanner[ip]['tcp'].keys())

elif menu == '2':
    print('Versão do nmap: ', scanner.nmap_version())
    scanner.scan(ip, '1-10', '-v -sU')
    print(scanner.scaninfo())
    print('Status do ip: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas abertas: ', scanner[ip]['udp'].keys())

elif menu == '3':
    print('Versão do nmao: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v sC')
    print('Status do ip: ', scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print('Portas abertas: ', scanner[ip]['tcp'].keys())

else:
    print('Escolha uma opção valida')




