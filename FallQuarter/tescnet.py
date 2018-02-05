#!/usr/bin/python
# tesc netcat lab (taken from blackhat python)

import sys
import socket
import getopt
import threading
import subprocess


# define some global variables
listen             = False
command            = False
upload             = False
execute            = ""
target             = ""
upload_destination = ""
port               = 0

# this runs a command and returns the output
def run_command(command):

    # trim the newline
                    command = command.rstrip()

                            # run the command and get the output back
                                    try:
                                                        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
                                                                except:
                                                                                    output = "Failed to execute command.\r\n"

                                                                                            # send the output back to the client
                                                                                                    return output

                                                                                                # this handles incoming client connections
                                                                                                def client_handler(client_socket):
                                                                                                            global upload
                                                                                                                    global execute
                                                                                                                            global command

                                                                                                                                    # check for upload
                                                                                                                                            if len(upload_destination):

                                                                                                                                                                # read in all of the bytes and write to our destination
                                                                                                                                                                                file_buffer = ""

                                                                                                                                                                                                # keep reading data until none is available
                                                                                                                                                                                                                while True:
                                                                                                                                                                                                                                            data = client_socket.recv(1024)

                                                                                                                                                                                                                                                                    if not data:
                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                file_buffer += data

                                                                                                                                                                                                                                                                                                                                                                                # now we take these bytes and try to write them out
                                                                                                                                                                                                                                                                                                                                                                                                try:
                                                                                                                                                                                                                                                                                                                                                                                                                            file_descriptor = open(upload_destination,"wb")
                                                                                                                                                                                                                                                                                                                                                                                                                                                    file_descriptor.write(file_buffer)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            file_descriptor.close()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    # acknowledge that we wrote the file out
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            client_socket.send("[+] Successfully saved file to %s\r\n" % upload_destination)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            except:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        client_socket.send("[!] Failed to save file to %s\r\n" % upload_destination)
