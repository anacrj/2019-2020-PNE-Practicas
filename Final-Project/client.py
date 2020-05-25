import http.client
import json

PORT = 8080
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))
conn = http.client.HTTPConnection(SERVER, PORT)

print("----TEST REPORT----")
print("====================")
print("")

# ---> MAIN PAGE
print("---> MAIN PAGE")
print("")
conn.request("GET", "/")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/")
print("* OUTPUT")
print(data1)
print("")


# ---> listSpecies endpoint
print("---> listSpecies endpoint")
print("")

print("Test 1")
print("")
conn.request("GET", "/listSpecies?limit=10")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/listSpecies?limit=10")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/listSpecies")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/listSpecies?limit")
print("* OUTPUT")
print(data1)
print("")


# ---> karyotype endpoint

print("---> karyotype endpoint")
print("")

print("Test 1")
conn.request("GET", "/karyotype?specie=mouse")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?specie=mouse")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
conn.request("GET", "/karyotype?spe=mouse")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?spe=mouse")
print("* OUTPUT")
print(data1)
print("")

print("Test 3")
conn.request("GET", "/karyotype?specie")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?specie=")
print("* OUTPUT")
print(data1)
print("")


# ---> chromosomeLength endpoint

print("---> chromosomeLength endpoint")
print("")

print("Test 1")
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=MT")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=mouse&chromo=MT")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/chromosomeLength?specie=hello&chromo")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=hello&chromo=")
print("* OUTPUT")
print(data1)
print("")

print("Test 3")
print("")
conn.request("GET", "/chromosomeLength?specie=&chromo=18")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=&chromo=18")
print("* OUTPUT")
print(data1)
print("")


# ---> genSeq endpoint

print("---> genSeq endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneSeq?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneSeq?gene=FRAT1")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/geneSeq?gene=10")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneSeq?gene=10")
print("* OUTPUT")
print(data1)
print("")


# ---> genInfo endpoint

print("---> genInfo endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneInfo?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneInfo?gene=FRAT1")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/geneInfo?gene=11")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneInfo?gene=11")
print("* OUTPUT")
print(data1)
print("")


# --->geneCalc endpoint

print("---> geneCalc endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneCalc?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneCalc?gene=FRAT1")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/geneCalc?gene=10")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneCalc?gene=10")
print("* OUTPUT")
print(data1)
print("")


# ---> geneList endpoint

print("---> geneList endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneList?chromo=7&start=3&end=30000")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=7&start=3&end=30000")
print("* OUTPUT")
print(data1)
print("")

print("Test 2")
print("")
conn.request("GET", "/geneList?chromo=&start=3&end=30000")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=&start=3&end=30000")
print("* OUTPUT")
print(data1)
print("")

print("Test 3")
print("")
conn.request("GET", "/geneList?chromo=hi&start=&end=30")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=hi&start=&end=30")
print("* OUTPUT")
print(data1)
print("")


# ----->>>>> JSON
print("------->>>> Attempts for JSON")

# 1) TRY FOR JSON
print("---> listSpecies endpoint")
print("")

print("Test 1")
conn.request("GET", "/listSpecies?limit=10json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/listSpecies?limit=10&json=1")
print("* OUTPUT")
print(response)
print("")

# ---> karyotype endpoint

print("---> karyotype endpoint")
print("")

print("Test 1")
conn.request("GET", "/karyotype?specie=mouse&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?specie=mouse&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/karyotype?specie=hello&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?specie=hello&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 3")
conn.request("GET", "/karyotype?specie=&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/karyotype?specie=&json=1")
print("* OUTPUT")
print(response)
print("")


# --->  chromosomeLength endpoint

print("---> chromosomeLength endpoint")
print("")

print("Test 1")
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=MT&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=mouse&chromo=MT&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/chromosomeLength?specie=hello&chromo=&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=hello&chromo=&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 3")
conn.request("GET", "/chromosomeLength?specie=&chromo=18&json=")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/chromosomeLength?specie=&chromo=18&json=1")
print("* OUTPUT")
print(response)
print("")


# --->  geneSeq endpoint

print("---> geneSeq endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneSeq?gene=FRAT1&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/geneSeq?gene=10&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneSeq?gene=10&json=1")
print("* OUTPUT")
print(response)
print("")


# --->  geneInfo endpoint

print("---> geneInfo endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneInfo?gene=FRAT1&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/geneInfo?gene=11&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneInfo?gene=11&json=1")
print("* OUTPUT")
print(response)
print("")


# --->  geneCalc endpoint

print("---> geneCalc endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneCalc?gene=FRAT1&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/geneCalc?gene=10&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneCalc?gene=10&json=1")
print("* OUTPUT")
print(response)
print("")


# --->  geneList endpoint

print("---> geneList endpoint")
print("")

print("Test 1")
conn.request("GET", "/geneList?chromo=7&start=3&end=30000&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=7&start=3&end=30000&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 2")
conn.request("GET", "/geneList?chromo=&start=3&end=30000&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=&start=3&end=30000&json=1")
print("* OUTPUT")
print(response)
print("")

print("Test 3")
conn.request("GET", "/geneList?chromo=hi&start=&end=30&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print("* INPUT: ")
print("http://127.0.0.1:8080/geneList?chromo=hi&start=&end=30&json=1")
print("* OUTPUT")
print(response)
print("")
