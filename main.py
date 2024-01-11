import socket  #Biblioteca para se comunicar com a placa de rede atravez do sistema operacional

ip = input('Digite o host ou ip a ser verificado : ')

ports = []
count = 0

while count < 10:
    ports.append(int(input('Digite a porta Desejada : ')))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INT conexão tipo ipv4
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))
    print(port)

    if code == 0:
        print(str(port), ' -> Porta aberta')
    else:
        print(str(port), ' -> Porta fechada')
