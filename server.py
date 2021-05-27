import socket
import tqdm
import connections as udpcon
from tqdm import tqdm
from time import sleep

HOST = '127.0.0.1'
PORT = 65432
print("connected to host...")

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(5)

    print("[+] Socket is listening")
    c, addr = s.accept()
    print('[+] Got connection from', addr, end="\n\n")
    print('Getting list of devices in range:')
    for i in tqdm(range(100)):
        # Waiting for 0.05 sec before next execution
        sleep(.05)
    print("Select the IP Address of the following connections : ")
    print("IP Address   " + "     :" + "    Name")
    for IP, Name in udpcon.udp.items():
        print(IP + "    :    " + Name)

    print("")

    while True:
        ip_req = c.recv(1024).decode()
        print("[+] Client requested IP : [", ip_req, "]")
        if ip_req == "quit":
            break
