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

        if len(self.data.split(',')[1])>1:
            print(f"messaggio: {self.data} - Difetti!")
            my_canvas.itemconfig(my_oval, fill="red") 
            label_var.set('Difetti trovati')  # Updating the label
        
        else:
            print(f"messaggio: {self.data} - Tutto OK!")
            my_canvas.itemconfig(my_oval, fill="green")  
            label_var.set('Tutto OK')  # Updating the label

            root.update()

if __name__ == "__main__":
    root = tk.Tk() 
    my_canvas = tk.Canvas(root, width=200, height=200)
    my_canvas.pack()
    my_oval = my_canvas.create_oval(50, 50, 100, 100)
    label_var = tk.StringVar() 
    my_label = tk.Label(root, textvariable=label_var)  
    my_label.pack()
    root.mainloop()

    HOST, PORT = "localhost", 8081
    print(f'\nPLC server online {HOST}:{PORT}\n')
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # interrupt the program with Ctrl-C
        server.serve_forever()



      

