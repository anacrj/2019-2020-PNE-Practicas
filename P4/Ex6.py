import socket
from pathlib import Path
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def get_resource(path):
    if path == "/info/A":
        response = Path("A.html").read_text()      # This contents are written in HTML language
    elif path == "/info/C":
        response = Path("C.html").read_text()      # This contents are written in HTML language
    elif path == "/info/G":
        response = Path("G.html").read_text()      # This contents are written in HTML language
    elif path == "/info/T":
        response = Path("T.html").read_text()      # This contents are written in HTML language
    elif path == "/info/":
        response = Path("index.html").read_text()  # This contents are written in HTML language
    else:
        response = Path("Error.html").read_text()  # This contents are written in HTML language
    return response


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    words = req_line.split(" ")

    # Get the method and path
    method = words[0]
    path = words[1]
    print(f"Method: {method}")
    print(f"Path: {path}")

    # Response body
    body = ""
    if method == "GET":
        body = get_resource(path)

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
