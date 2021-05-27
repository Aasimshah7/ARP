import socket

import connections as udpcon
from tqdm import tqdm
from time import sleep

HOST = '127.0.0.1'
PORT = 65432

with socket.socket() as s:
    s.connect((HOST, PORT))

    print("Host has the following connections : ")
    print("IP Address \t " + "     :" + "    Name")
    for IP, Name in udpcon.udp.items():
        print(IP + "    :    " + Name)

    print("")

    while True:
        print("")
        req_ip = input("Request Mac Address for IP : ")
        s.sendall(req_ip.encode())
        if req_ip == "quit":
            break
        if req_ip in udpcon.con:
            for i in tqdm(range(100)):
                # Waiting for 0.01 sec before next execution
                sleep(.01)
            print("IP Address        :   ", "Mac Address                              :    Name")
            print(req_ip, "   :   ", udpcon.con[req_ip], "    :   ", udpcon.udp[req_ip])
        else:
            print("[+] Invalid Request No such connection found.")


