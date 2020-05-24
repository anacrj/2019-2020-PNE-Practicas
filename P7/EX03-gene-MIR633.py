import http.client
import json
import termcolor

genes = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060", "RNU6-269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

gene_name = "MIR633"
server = "rest.ensembl.org"
end_point = "/sequence/id/"
parameters = "?content-type=application/json"
request = end_point + genes[gene_name] + parameters
URL = server + request

print()
print(f"Server: {server}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", request)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data, form the JSON received
gene = json.loads(data1)

print()
termcolor.cprint("Gene: ", 'green', end="")
print(gene_name)
termcolor.cprint("Description: ", 'green', end="")
print(gene["desc"])
termcolor.cprint("Bases: ", 'green', end="")
print(gene["seq"])

