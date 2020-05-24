from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

# Test PING
print("* Testing PING...")
print(c.talk("PING"))

# Test GET
print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

# Test "INFO"
print("* Testing INFO...")
s = c.talk("GET 0")
function = f"INFO {s}"
print(c.talk(function))

# Test 4: COMPLEMENT
print("* Testing COMPLEMENT...")
function = f"COMP {s}"
print(c.talk(function))

# Test 5: REVERSE
print("* Testing REVERSE...")
function = f"REV {s}"
print(c.talk(function))

# Test 6: "GENE"
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    print("GENE" + c.talk(gene))
