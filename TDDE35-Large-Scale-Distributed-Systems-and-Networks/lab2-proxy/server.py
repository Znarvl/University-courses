import socket, time, sys
import select
import queue

HOST = "127.0.0.1"  # Proxy server IP (localhost)
PORT = 1234         # Proxy server port
max_conn = 5
buffer_size = 8192

bad_words = ["SpongeBob", "spongebob", "britney spears", "Britney Spears",
            "paris hilton", "Paris Hilton", "norrköping", "Norrköping",
            "norrkoping", "Norrkoping"]

def start():
    """ Starts the proxy server. Runs NetNinny for bad URL."""
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #server.gethostbyname("")
        server.bind((HOST, PORT))
        server.listen(max_conn)
        print("Server Started Successfully [%d]\n" % (PORT))
    except Exception as e:
        print ("Unable To Initialise Socket")
        sys.exit(2)

    while True:
        try:
            conn, addr = server.accept()
            data = conn.recv(buffer_size)
            header, webserver = get_header(data)
            with conn:
                if bad_url(header):
                    redirect_bad_url(conn)
                else:
                    proxy_server(webserver, 80, conn, addr, header)
            print("Just like the simulations.")
        except KeyboardInterrupt:
            server.close()
            print ("\n Proxy Server Closed by KeyboardInterrupt")
            sys.exit(1)
        except TypeError as msg:
            print(msg)
            sys.exit(1)
    server.close()


def get_header(data):
    """ Grabs the header from the data.
        Removes host info from the GET line, changes Accept-Encoding to identity,
        and Connection to Connection: close."""
    header = data.split(b'\r\n\r\n')[0]
    header = header.decode("utf-8")
    lines = header.split('\r\n')
    webserver = ""
    for line in lines:
        if '://' in line:
            req_type = line.split(' ')[0]
            rel_url = line.split('://')[1]
            rel_url = req_type+' '+rel_url[rel_url.find('/'):]
            lines[lines.index(line)] = rel_url
        if 'Host:' in line:
            webserver = line.split(' ')[1]
        if 'Accept-Encoding' in line:
            encoding = "Accept-Encoding: identity"
            lines[lines.index(line)] = encoding
        if 'Connection' in line:
            connection = "Connection: close"
            lines[lines.index(line)] = connection
    new_header = ""
    for line in lines:
        new_header += line
        new_header += '\r\n'
    new_header += '\r\n'
    print(new_header)
    return new_header, webserver


def get_content(data):
    """ Splits off the content from the message, if any content exists.
        Returns a bytes-like object."""
    content = data.split(b'\r\n\r\n')
    if len(content) > 1:
        content = content[1]
    else:
        content = b""
    return content

def redirect_bad_url(conn):
    print("These are not the droids you are looking for.")
    relocate = b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://zebroid.ida.liu.se/error1.html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'
    conn.sendall(relocate)

def redirect_bad_content(conn):
    print("These are not the droids you are looking for.")
    relocate = b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://zebroid.ida.liu.se/error2.html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'
    conn.sendall(relocate)

def bad_url(url):
    """ Checks if any of the forbidden words exist in the url string."""
    for word in bad_words:
        if word in url:
            return True
    return False

def bad_content(words):
    """ Checks if any of the forbidden words exist in the content string."""
    words = words.decode()
    for word in bad_words:
        if word in words:
            #print(words)
            return True
    return False

def proxy_server(webserver, port, conn, addr, data):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((webserver, port))
        sock.send(data.encode('utf-8')) # Initial GET Request
        sock.settimeout(30)
        response_text = b""
        while True:
            try:
                response = sock.recv(buffer_size)
                if response is not None and len(response) == 0:
                    break
                response_text += response
            except:
                print("It's a trick, send no reply")
                break
            if len(response_text) >= 10485760:
                print("Sending chunk")
                if b'text' in response_text:
                    content_text = get_content(response_text)
                    if bad_content(content_text):
                        print("found baddies")
                        redirect_bad_content(conn)
                        break
                conn.sendall(response_text)
                response_text = b""

        if b'text' in response_text:
            content_text = get_content(response_text)
            if bad_content(content_text):
                print("found baddies")
                response_text = b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://zebroid.ida.liu.se/error2.html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'
        conn.sendall(response_text)

    except socket.error as msg:
        print("Sector is clear.")
        print("NOT CLEAR! NOT CLEAR!")
        print("Socket Exception: ", msg)
        sock.close()
        conn.close()
        sys.exit(1)

start()
