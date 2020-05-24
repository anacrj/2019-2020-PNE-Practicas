import http.server
import socketserver
import termcolor
import json
import http.client
from Seq1 import Seq

PORT = 8080


# -- Class with our Handler. It is a called derived from BaseHTTPRequestHandler.
# -- It means that our class inheritates all his methods and properties

class TestHandler(http.server.BaseHTTPRequestHandler):
    # Function used to implement JSON (treats any type of parameter that can have an endpoint)

    def dictionary_split(self, path):
        dictionary = dict()
        dicc = self.path.split("?")        # The path has at least one variable (argument)
        if len(dicc) > 1:
            args = dicc[1]
            dicc = args.split(" ")[0]
            parts = dicc.split("&")

            for couple in parts:
                if '=' in couple:
                    aux = couple.split("=")
                    key = aux[0]
                    value = aux[1]
                    dictionary[key] = value             # Associate a value to each key
        return dictionary

    def do_GET(self):          # This method is called when the client invokes the GETmethod in the HTT Protocol request
        response_code = 200    # Indicates what happened with the request
        json_response = False  # Response only in HTML at the moment

        if self.path == "/":
            with open("index.html", "r") as f:
                contents = f.read()
            f.close()

        elif "listSpecies" in self.path:
            dicc = self.dictionary_split(self.path)
            limit = 0
            if 'limit' in dicc:
                try:
                    limit = int(dicc['limit'])
                except:
                    limit = 0

            conn = http.client.HTTPConnection('rest.ensembl.org')                 # Connection with Enssembl
            conn.request("GET", "/info/species?content-type=application/json")
            r1 = conn.getresponse()                                               # Get the response
            text_json = r1.read().decode("utf-8")                 # Decode the response in utf-8 format (admit all characters in the response)
            response = json.loads(text_json)
            print(response)

            species = response['species']
            if 'json' in dicc and dicc['json'] == '1':
                json_response = True
                if limit == 0:
                    limit = len(species)
                final_list = species[1:limit]      # List from the first specie until the one that corresponds to the limit
                contents = json.dumps(final_list)  # json.dumps is for transforming final_list into JSON (JSON response)
            else:
                if limit == 0:
                    limit = len(species)

                # HTML response
                contents = """ 
                                        <html>
                                        <head>
                                          <meta charset="utf-8">
                                          <title>Species in genome database</title>
                                        </head>
                                        <body style ="background-color: lightgrey;">
                                        <h3>List with the species available in the database:</h3>
                                        <ol> """

                # List with the name of all species
                cont = 0
                for specie in species:
                    cont = cont + 1
                    if cont <= limit:                             # The loop will not concatenate more species when it reaches the limit
                        contents = contents + "<li>" + specie['display_name'] + "</li>"
                contents = contents + """<ol>
                                        <body>
                                        <html>
                                        """
            conn.close()

        elif "karyotype" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'specie' in dicc and dicc['specie'] != '':
                specie = dicc['specie']
                conn = http.client.HTTPConnection('rest.ensembl.org')              # Connection with Enssembl
                conn.request("GET", "/info/assembly/" + specie + "?content-type=application/json")
                r1 = conn.getresponse()                                            # Get the response
                text_json = r1.read().decode("utf-8")                              # Decode the response in utf-8 format
                response = json.loads(text_json)                                   # Transform JSON into a Python value (to read JSON response)

                # Enter in the karyotype key
                if 'karyotype' in response:
                    list_chromo = response['karyotype']                            # List with all genes
                    if 'json' in dicc and dicc['json'] == '1':
                        json_response = True
                        contents = json.dumps(list_chromo)             # Transform list_chromo into JSON (JSON response)
                    else:

                        # HTML response
                        contents = """
                                    <html>
                                    <head>
                                      <meta charset="utf-8">
                                      <title>Information karyotype</title>
                                    </head>
                                    <body style ="background-color: lightblue;">
                                    <h2>Information about the karyotype of the chosen specie:</h2>
                                    <ul> """

                        for chromo in list_chromo:
                            new_chromo = "<li>" + chromo + "</li>"
                            contents = contents + new_chromo          # List with elements from list_chromo

                        contents += """</ul>
                                    </body>
                                    </html>
                                    """
                else:
                    response_code = 404
                    f = open('error.html', 'r')
                    contents = f.read()
                    f.close()
            else:
                response_code = 404
                f = open('error.html', 'r')
                contents = f.read()
                f.close()

        elif "chromosomeLength" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'chromo' in dicc and 'specie' in dicc and dicc['chromo'] != '' and dicc['specie'] != '':
                chromo1 = dicc['chromo']
                specie = dicc['specie']
                conn = http.client.HTTPConnection('rest.ensembl.org')                        # Connection with Enssembl
                conn.request("GET", "/info/assembly/" + specie + "?content-type=application/json")
                r1 = conn.getresponse()                                                      # Get the response
                text_json = r1.read().decode("utf-8")                                        # Decode the response in utf-8 format
                response = json.loads(text_json)                                             # Transform JSON into a Python value (to read JSON response)

                # Enter into the key top_level_region to obtain the length of the chromosome
                info = response['top_level_region']                                          # List to save all the chromosomes
                if 'json' in dicc and dicc['json'] == '1':
                    json_response = True
                    long = 0
                    for element in info:
                        if element['name'] == chromo1:
                            long = element['length']
                    dic = dict()
                    dic['len'] = long
                    contents = json.dumps(dic)                                 # Transform dic into JSON (JSON response)
                else:
                    long = 0
                    for element in info:
                        if element['name'] == chromo1:
                            long = element['length']

                    # HTML response
                    contents = """
                                           <html>
                                           <head>
                                             <meta charset="utf-8">
                                             <title>Length of the chromosome</title>
                                           </head>
                                           <body style ="background-color: lightyellow;">
                                           <h3>The length of the chromosome is:</h3>
                                           <ul> """

                    contents = contents + "<li>" + str(long) + "</li>"
                    contents = contents + """</ul>
                                            </body>
                                            </html>"""
            else:
                response_code = 404
                f = open('error.html', 'r')
                contents = f.read()
                f.close()

        elif "geneSeq" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'gene' in dicc and dicc['gene'] != '':
                gene = dicc['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')                             # Connection with Enssembl
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()                                                           # Get the response
                raw_data = r1.read().decode("utf-8")                                              # Decode the response in utf-8 format
                response = json.loads(raw_data)                                                   # Transform JSON into a Python value (to read JSON response)
                try:
                    id = response['data'][0]['id']                                               # Get the id of the data
                    url ="/sequence/id/" + id + "?content-type=application/json"
                    conn.request("GET", url)
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")
                    response = json.loads(text_json)
                    cadena = response['seq']

                    if 'json' in dicc and dicc['json'] == '1':
                        json_response = True
                        dic = dict()
                        dic['seq'] = cadena
                        contents = json.dumps(dic)                                            # Transform dic into JSON (JSON response)
                    else:

                        # HTML response
                        contents = """
                                                           <html>
                                                           <head>
                                                             <meta charset="utf-8">
                                                             <title>Sequence of the gene</title>
                                                           </head>
                                                           <body style ="background-color: lightgreen;">
                                                           <font face="garamond"  color = "black"</font>
                                                           <h2>This is the sequence of the human gene requested:</h2>
                                                           <ul> """
                        contents += "<ul>"
                        contents += cadena + "<ul>"
                        contents += """</ul>
                                                            </body>
                                                            </html>"""
                except KeyError:
                    response_code = 404
                    f = open('error.html', 'r')
                    contents = f.read()
                    f.close()
            else:
                response_code = 404
                f = open('error.html', 'r')
                contents = f.read()
                f.close()

        elif "geneList" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'start' in dicc and 'chromo' in dicc and 'end' in dicc and dicc['start'] != '' and dicc['chromo'] != '' and dicc['end'] != '':
                start = dicc['start']
                chromo = dicc['chromo']
                end = dicc['end']
                conn = http.client.HTTPConnection('rest.ensembl.org')                                          # Connection with Enssembl
                conn.request("GET", "/overlap/region/human/" + str(chromo) + ":" + str(start) + "-" + str(
                    end) + "?content-type=application/json;feature=gene")
                r1 = conn.getresponse()                                                                        # Get the response
                data1 = r1.read().decode("utf-8")                                                              # Decode the response in utf-8 format
                response = json.loads(data1)                                                                   # Transform JSON into a Python value (to read JSON response)

                if 'error' in response:
                    response_code = 404
                    f = open('error.html', 'r')
                    contents = f.read()
                    f.close()
                else:
                    if 'json' in dicc and dicc['json'] == '1':
                        json_response = True
                        lista = []
                        for item in response:
                            dic = dict()
                            dic['external_name'] = item['external_name']
                            dic['start'] = str(item['start'])
                            dic['end'] = str(item['end'])
                            lista.append(dic)                                                             # Create a list with those elements
                        contents = json.dumps(lista)                                                      # Transform lista into JSON (JSON response) (to read JSON response)
                    else:
                        print(response)

                        # HTML response
                        contents = """
                                                          <html>
                                                          <head>
                                                            <meta charset="utf-8">
                                                            <title>Gene information</title>
                                                          </head>
                                                          <body style ="background-color: lightgrey;">
                                                          <font face="garamond"  color = "black"</font>
                                                          <h2>Name, start and end of the genes located in the desired chromosome:</h2>
                                                          <ul> """
                        for item in response:
                            contents = contents + "<li>" + item['external_name'] + " Start: " + str(item['start']) + " End: " + str(item['end']) + "</li>"
                        contents = contents + """</ul>
                                                          </body>
                                                          </html>"""
            else:
                response_code = 404
                f = open('error.html', 'r')
                contents = f.read()
                f.close()

        elif "geneInfo" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'gene' in dicc and dicc['gene'] != '':
                gene = dicc['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')                                    # Connection with Enssembl
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()                                                                  # Get the response
                raw_data = r1.read().decode("utf-8")                                                     # Decode the response in utf-8 format
                response = json.loads(raw_data)                                                          # Transform JSON into a Python value (to read JSON response)
                try:
                    id = response['data'][0]['id']                                                       # Get the id of the data
                    conn.request("GET", "/overlap/id/" + id + "?feature=gene;content-type=application/json")
                    r1 = conn.getresponse()
                    raw_data = r1.read().decode("utf-8")
                    response = json.loads(raw_data)
                    start = response[0]['start']
                    end = response[0]['end']
                    id = response[0]['id']
                    lenght = end - start
                    chromo = response[0]['assembly_name']

                    if 'json' in dicc and dicc['json'] == '1':
                        json_response = True
                        dic = dict()
                        dic['id'] = id
                        dic['start'] = start
                        dic['end'] = end
                        dic['lenght'] = lenght
                        contents = json.dumps(dic)
                    else:

                        # HTML response
                        contents = """
                                                                        <html>
                                                                        <head>
                                                                          <meta charset="utf-8">
                                                                          <title>Human gene information</title>
                                                                        </head>
                                                                        <body style ="background-color: lightyellow;">
                                                                       <font face="garamond" size = 5 color = "black"</font>
                                                                       <h3>Information about the human gene requested:</h3>
                                                                       <ul> """

                        contents = contents + "<h4>Id: <h4>" "<li>" + id + "</li>"
                        contents = contents + "<h4>Start: <h4>" "<li>" + str(start) + "</li>"
                        contents = contents + "<h4>End: <h4>" "<li>" + str(end) + "</li>"
                        contents = contents + "<h4>Length: <h4>" "<li>" + str(lenght) + "</li>"
                        contents = contents + "<h4>Chromosome: <h4>""<li>" + chromo + "</li>"
                        contents = contents + """</ul>
                                                                        </body>
                                                                        </html>"""
                except KeyError:
                    response_code = 404
                    f = open('error.html', 'r')
                    contents = f.read()
                    f.close()
            else:
                response_code = 404
                f = open('error.html', 'r')
                contents = f.read()
                f.close()

        elif "geneCalc" in self.path:
            dicc = self.dictionary_split(self.path)
            if 'gene' in dicc and dicc['gene'] != '':
                gene = dicc['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')                                    # Connection with Enssembl
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()                                                                  # Get the response
                raw_data = r1.read().decode("utf-8")                                                     # Decode the response in utf-8 format
                response = json.loads(raw_data)                                                          # Transform JSON into a Python value (to read JSON response)
                try:
                    id = response['data'][0]['id']                                                       # Get the id of the data
                    conn.request("GET", "/sequence/id/" + id + "?content-type=application/json")
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")
                    response = json.loads(text_json)
                    cadena = response['seq']

                    s1 = Seq(cadena)
                    total = len(cadena)
                    percA = s1.perc('A')
                    percT = s1.perc('T')
                    percG = s1.perc('G')
                    percC = s1.perc('C')

                    if 'json' in dicc and dicc['json'] == '1':
                        json_response = True
                        dic = dict()
                        dic['lenght'] = total
                        dic['percA'] = percA
                        dic['percT'] = percT
                        dic['percG'] = percG
                        dic['percC'] = percC
                        contents = json.dumps(dic)
                    else:

                        # HTML contents
                        contents = """
                                                                                 <html>
                                                                                <head>
                                                                                  <meta charset="utf-8">
                                                                                  <title>Calculations</title>
                                                                                </head>
                                                                                <body style ="background-color: lightgreen;">
                                                                                <font face="garamond" size = 5 color = "black"</font>
                                                                                <h2>Calculations about the human gene:</h2>
                                                                                 <ul> """

                        contents = contents + "<h3>Lenght: <h4>" "<li>" + str(total) + "</li>"
                        contents = contents + "<h4>Percentage of A: <h4>" "<li>" + str(percA) + "</li>"
                        contents = contents + "<h4>Percenatge of T: <h4>" "<li>" + str(percT) + "</li>"
                        contents = contents + "<h4>Percenatge of G: <h4>" "<li>" + str(percG) + "</li>"
                        contents = contents + "<h4>Percenatge of C: <h4>""<li>" + str(percC) + "</li>"
                        contents = contents + """</ul>
                                                                                      </body>
                                                                                      </html>"""
                except KeyError:
                    response_code = 404
                    with open("error.html", "r") as f:
                        contents = f.read()
            else:
                response_code = 400
                with open("error.html", "r") as f:
                    contents = f.read()
        else:
            response_code = 404
            with open("error.html", "r") as f:
                contents = f.read()

        # -- Generating the response message
        self.send_response(response_code)
        if (json_response == True):                               # Define the content-type header
            self.send_header('Content-Type', 'application/json')
        else:
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(str.encode(contents)))

        # -- The header is finished
        self.end_headers()

        # -- Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True     # For preventing the error: "Port already in use"

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
