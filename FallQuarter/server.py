#!/usr/bin/python
# tesc networking tcp server exercise (taken from blackhat python)
# fill in the missing code

import socket
import threading
bind_ip = "10.10.10.10"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allow listening despite TIME_WAIT sockets
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind to ip & port
server_address = ('localhost', 9999)
server.bind(server_address)
# [enter code here]

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# this is our client handling thread
def handle_client(client_socket):

        # just print out what the client sends
            request = client_socket.recv(1024)

                print "[*] Received: %s" % request

                    # send back a packet
                        client_socket.send("ACK\n")
                            print client_socket.getpeername()
                                client_socket.close()


                                while True:

                                        # accept a connection
                                            client, addr = server.accept()
                                                # client,addr = [enter code here]

                                                    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

                                                        # spin up our client thread to handle incoming data
                                                            client_handler = threading.Thread(target=handle_client,args=(client,))
                                                                client_handler.start()
