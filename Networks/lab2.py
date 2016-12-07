import os, sys, socket, requests
MAX_BYTES = 65533

# Source: http://stackoverflow.com/a/519653
def read_in_chunks(file_object, chunk_size=1024):
    """ Generator to read a file piece by piece. """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def client(newFile, fileToCopy, host="localhost", port=6900):
    infolist = socket.getaddrinfo(host, port, 0, socket.SOCK_DGRAM, 0,
                    socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)

    info = infolist[0]
    sock_args = info[0:3]
    address = info[4]

    sock = socket.socket(*sock_args)
    sock.connect(address)

    sock.send(newFile.encode('ascii'))

    with open(fileToCopy, 'r') as f:
        for chunk in read_in_chunks(f):
            sock.send(chunk.encode('ascii'))

    sock.send(''.encode('ascii'))
    sock.close()

def server(host='localhost', port=6900):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', port))
    print ('Listening at {}'.format(sock.getsockname()))

    data, address = sock.recvfrom(MAX_BYTES)
    newFileName = data.decode('ascii')

    with open(newFileName, 'w') as f:
        while True:
            data, address = sock.recvfrom(MAX_BYTES)
            text = data.decode('ascii')
            f.write(text)
            if text == '':
                break

if len(sys.argv) < 1:
    print ('Please specify whether to run this as the client or server')
    sys.exit(-2)

if 's' in sys.argv[1] or 's' in sys.argv[1]:
    server()

if 'c' in sys.argv[1] or 'C' in sys.argv[1]:

    if len(sys.argv) < 3:
        print ('Downloading and transferring beowulf')
        r = requests.get('http://www.gutenberg.org/cache/epub/16328/pg16328.txt')
        with open('beowulf.txt', 'w') as f:
            f.write(r.text.encode('ascii', 'ignore'))
        client ('beowulf-copy.txt', 'beowulf.txt')
    else:
        client(sys.argv[2]+'-copy.txt', sys.argv[2])

print('Closing script')
sys.exit(0)
