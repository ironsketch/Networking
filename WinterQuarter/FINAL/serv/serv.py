#!/usr/bin/python

import socket, signal, time

class Server:
    def __init__(self, port = 80):
        self.host = ''
        self.port = port
        self.www_dir = 'www'

    def activate(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Launching server on: ", self.host, ":", self.port)
            self.socket.bind((self.host, self.port))
        except Exception as e:
            print("Could not get port: ", self.port, "\n")
            user_port = self.port
            self.port = 8080

            try:
                print("Launching server on: ", self.host, ":", self.port)
                self.socket.bind((self.host, self.port))
            except Exception as e:
                print("Failed again.")
                self.shutdown()
                import sys
                sys.exit(1)

        print("Successfull.")
        self._wait_for_connections()

    def shutdown(self):
        try:
            print("Shutting Down...")
            s.socket.shutdown(socket.SHUT_RDWR)
        except Exception as e:
            print("Failed shutting down socket.")

    def _gen_headers(self, code):
        h = ''

