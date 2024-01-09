import socket, config
from threading import Thread
from query import Database

db = Database('postgres', 'localhost','ChatRoom','admin12345')
db.connect()

def login(client, username, password):
        if db.login(username, password):
            print(f"[+] {client.getpeername()} logged in as {username}")
            client.send("LOGIN_SUCCESS".encode('utf-8'))
        else:
            print(f"[-] Login failed for {username}")
            client.send("LOGIN_FAILURE".encode('utf-8'))
            
def signup(client, username, password):
    if db.signup(username, password):
        print(f"[+] {client.getpeername()} signed up as {username}")
        client.send("SIGNUP_SUCCESS".encode('utf-8'))
    else:
        print(f"[-] Signup failed for {username}")
        client.send("SIGNUP_FAILURE".encode('utf-8'))

def listen_for_client(clients, client):

    while True:
        try:
            msg = client.recv(config.BUFFER_SIZE).decode()
            
            if not msg:
                raise ConnectionError("Client disconnected")
        except ConnectionError as ce:
            clients.remove(client)
            print(f"[-] {client.getpeername()} disconnected. Reason: {ce}")
            break
        except socket.error as se:
            clients.remove(client)
            print(f"[-] Socket error for {client.getpeername()}: {se}")
            break
        except Exception as e:
            print(f"[-] Error while receiving data from {client.getpeername()}: {e}")
            clients.remove(client)
            break

        if msg.startswith("LOGIN:"):
            credentials = msg[len("LOGIN:"):].split(":") 
            username, password = credentials[0], credentials[1]
            login(client, username, password)

        elif msg.startswith("SIGNUP:"):
            credentials = msg[len("SIGNUP:"):].split(":")
            username, password = credentials[0], credentials[1]
            signup(client, username, password)
            
        else:
            for client_socket in clients:
                client_socket.send(msg.encode())

def main():
    client_sockets = set()   
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((config.SERVER_HOST, config.SERVER_PORT))
    server.listen()
    print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"[+] {client_address} connected.")
        client_sockets.add(client_socket)
        client_thread = Thread(target=listen_for_client, args=(client_sockets, client_socket))
        client_thread.daemon = True
        client_thread.start()
        print(len(client_sockets))

main()

