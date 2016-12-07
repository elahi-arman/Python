import random, socket, sys
MAX_BYTES = 65533

class Server():
    """docstring for Server."""
    def __init__(self, port=6900):
        print('Initializing Server')

        # creates the plain socket object which is unbound.
        # if you try to communicate it will raise an error
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # bind is actually used to request a UDP network address
        # this is represented by a tuple (str:hostname/addr, int:port)
        # this step can fail if the address is already in use
        # we can change this to 0.0.0.0 which binds to any local interface
        # this is an explicitly bound socket
        self.sock.bind(('localhost', port))

        # the sock.getsockname() retrieves a tuple contianing current IP addr &
        # port to which the socket is currently bound
        print('Listening at {}'.format(self.sock.getsockname()))

        self.receive_infinitely()

    def receive_infinitely(self):
        while True:
            data, address = self.sock.recvfrom(MAX_BYTES)
            text = data.decode('ascii')
            print('The client at {} says {!r}'.format(address, text))
            text = 'Your data was {} bytes long'.format(len(data))
            data = text.encode('ascii')
            self.sock.sendto(data, address)

    def receive_randomly_drop(self):
        while True:
            data, address = self.sock.recvfrom(MAX_BYTES)

            # mocking a dropped packet
            if random.random() < 0.5:
                print('Pretending emto drop last packet from {}'.format(address))
                continue

            text = data.decode('ascii')
            print('The client at {} says {!r}'.format(address, text))
            text = 'Your data was {} bytes long'.format(len(data))
            data = text.encode('ascii')
            self.sock.sendto(data, address)

class Client():
    """docstring for Client."""
    def __init__(self, host="localhost", port=6900):
        print('Initializing Client')
        infolist = socket.getaddrinfo(host, port, 0, socket.SOCK_DGRAM, 0,
                        socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)

        info = infolist[0]
        sock_args = info[0:3]
        address = info[4]

        self.sock = socket.socket(*sock_args)
        self.sock.connect(address)
        self.send_once()



    def send_with_retry(self, delay, host, port):

        # allows us to use send no need to explicitly state address every time
        # it also means that the client is not in promiscuous mode now
        # the OS will discard incoming packets to the port whose return
        # address doesn't match the address we've connected to
        # but connect only allows us to communicate with one server at a time
        # per socket
        print('Connected to server {!r}'.format(self.sock.getpeername()))

        current_delay = 0.1
        data = 'Here is a message'.encode('ascii')
        while True:
            sock.send(data)
            print ('Waiting up to {} seconds for a reply'.format(delay))
            sock.settimeout(delay)

            try:
                data = sock.recv(MAX_BYTES)
            except socket.timeout:
                current_delay *= 2          # exponential backoff, sending less and less frequently
                if current_delay > delay:
                    raise RuntimeError('Server is possible down')
                else:
                    break

        print('The server says {!r}'.format(data.decode('ascii')))

    def send_once(self):
        text = 'Hurro'

        # the sendto needs both a message and a destination address
        # this is the entirety of what we need to communicate with ourself
        self.sock.send(text.encode('ascii'))

        # to actually communicate the client needs to also have a name and address
        # for purposes of Lab 2 we don't really care about this, but it's nice
        # to have. This is automatically assigned by the OS

        # here we have an implicitly bound socket
        print('The OS assignmed me the address {}'.format(self.sock.getsockname()))

        # note that we don't do any address sanitization so if you look at your
        # neighbor's stuff, they can intercept and possibly send malicious data
        # data, address = self.sock.recvfrom(MAX_BYTES)
        # text = data.decode('ascii')
        # print('The server P replied {!r}'.format(address, text))

if len(sys.argv) < 1:
    print ('Please specify whether to run this as the client or server')
    sys.exit(-2)

if 's' in sys.argv[1] or 's' in sys.argv[1]:
    server = Server()

if 'c' in sys.argv[1] or 'C' in sys.argv[1]:
    client = Client()

print('Closing script')
sys.exit(0)
