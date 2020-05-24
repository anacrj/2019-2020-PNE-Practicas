import http.client
import json

SERVER = "rest.ensembl.org"
Endpoint = "info/ping"
Parameters = "?content-type=application/json"
URL = SERVER + Endpoint + Parameters

print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# Send the request message, using the GET method.
try:
    conn.request("GET", Endpoint + Parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()        # Read the response message from the server

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data in the form received: JSON
response = json.loads(data1)

ping_endpoint = response["ping"]
if ping_endpoint == 1:
    print("PING OK! The database is running!")
