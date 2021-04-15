from Client0 import Client

PORT = 8080
IP = "192.168.1.136"

for i in range(5):
    c = Client(IP, PORT)
    c.debug_talk(f"Message{i}")