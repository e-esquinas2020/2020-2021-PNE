import socket
import termcolor

IP = "192.168.1.136"
PORT = 8080
num_con = 0
list_con = []

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.listen()
print("Server is configured")

while num_con < 5:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        num_con = num_con + 1
        print(f"CONNECTIONS{num_con}. Client IP,PORT {client_ip_port}")
        list_con.append(client_ip_port)
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Received Message:", end="")
        termcolor.cprint(msg, "green")

        response = "ECHO: " + msg + "\n"
        cs.send(response.encode())
        cs.close()

print("The following clients has connected to the server: ")
for i, c in enumerate(list_con):
    print(f"Client {i}: {c}")
ls.close()