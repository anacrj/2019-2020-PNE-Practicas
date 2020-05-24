import http.client
import json
import termcolor
from Seq1 import Seq

bases = ["A", "C", "T", "G"]
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

termcolor.cprint("Gene", 'green', end="")
print(f": {gene_name}")
termcolor.cprint("Description", 'green', end="")
print(f": {gene['desc']}")

gene_seq = gene['seq']

# -- Create the object sequence from the string
s = Seq(gene_seq)

sl = s.len()
ac = s.count_base('A')
ap = "{:.1f}".format(100 * ac / sl)
cc = s.count_base('C')
pc = "{:.1f}".format(100 * cc / sl)
gc = s.count_base('G')
pg = "{:.1f}".format(100 * gc / sl)
ct = s.count_base('T')
pt = "{:.1f}".format(100 * ct / sl)

termcolor.cprint("Total lengh", 'green', end="")
print(f": {sl}")

termcolor.cprint("A", 'blue', end="")
print(f": {ac} ({ap}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {cc} ({pc}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {gc} ({pg}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {ct} ({pt}%)")

# -- Dictionary with the values
d = s.count()

# -- Create a list with all the values
ll = list(d.values())

# -- Calculate the maximum
m = max(ll)

# -- Print the base
termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {bases[ll.index(m)]}")