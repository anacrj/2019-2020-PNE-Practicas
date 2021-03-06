from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)
# -- Print the IP and PORTs
print(c)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
# First we have to launch the Teacher's server of Session-08 (server.py). Then execute the EX3.py program.
