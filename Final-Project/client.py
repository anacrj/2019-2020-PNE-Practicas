import http.client
import json

PORT = 8080
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))
conn = http.client.HTTPConnection(SERVER, PORT)

print("----Test report---")
print("====================")
print("")
print("---> listSpecies endpoint")
print("")
print("Test 1")
conn.request("GET", "/listSpecies")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)
print("")
print("Test 2")
conn.request("GET", "/listSpecies?limit=10")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> karyotype endpoint")
conn.request("GET", "/karyotype?specie=mouse")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> chromosomeLength endpoint")
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> genSeq endpoint")
conn.request("GET", "/geneSeq?gene=FRAT1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> genInfo endpoint")
conn.request("GET", "/geneInfo?gene=FRAT1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> geneCal endpoint")
conn.request("GET", "/geneCal?gene=FRAT1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)

print("---> geneList endpoint")
conn.request("GET", "/geneList?chromo=1&start=0&end=30000")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
print(data1)


# ----- JSON

# 1) TRY FOR JSON
conn.request("GET", "/listSpecies?json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 2) TRY FOR JSON
conn.request("GET", "/karyotype?specie=mouse&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 3) TRY FOR JSON
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 4) TRY FOR JSON
conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 5) TRY FOR JSON
conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 6) TRY FOR JSON
conn.request("GET", "/geneCal?gene=FRAT1&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)

# 7) TRY FOR JSON
conn.request("GET", "/geneList?chromo=1&start=0&end=30000&json=1")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print(response)
