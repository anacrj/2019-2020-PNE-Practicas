import socket
import termcolor

IP = "192.168.56.1"
PORT = 8080

# --- 1) Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- 2) Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- 3) Step 3: Convert into a listening socket
ls.listen()

print(" The Server is configured!")

while True:

    try:
        # 4) Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:           # Server stopped manually
        print("Server is done!")
        ls.close()
        exit()
    else:
        # 5) Step 5: Receiving information from the client
        print("A client has connected to the server!")
        msg_raw = cs.recv(2000)         # Received message is in raw bytes
        msg = msg_raw.decode()          # We decode it for converting it into a human-redeable string

        print("Received message:", end="")
        termcolor.cprint(f"{msg}", "green")

        # Step 6: Send a response message to the client
        response = "ECHO: " + msg + "\n"

        cs.send(response.encode())
        cs.close()
