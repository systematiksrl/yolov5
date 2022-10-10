import time
import socketserver
from datetime import datetime
import tkinter as tk

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip() # self.request is the TCP socket connected
        print(f"\nIP connesso   -> {self.client_address[0]}")
        print(f"dati ricevuti -> {self.data}")
        print(datetime.now())

if __name__ == "__main__":

    HOST, PORT = "localhost", 8081
    print(f'\nPLC server online {HOST}:{PORT}\n')
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # interrupt the program with Ctrl-C
        server.serve_forever()



      

