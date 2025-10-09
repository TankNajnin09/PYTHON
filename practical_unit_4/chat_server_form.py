import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# ---------------- GUI + Server -----------------
class ChatServer:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Chat")
        self.master.geometry("400x500")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)

        self.msg_entry = tk.Entry(master)
        self.msg_entry.pack(padx=10, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_msg)

        self.send_btn = tk.Button(master, text="Send", command=self.send_msg)
        self.send_btn.pack(pady=5)

        threading.Thread(target=self.start_server, daemon=True).start()

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 9999))
        self.server.listen(1)
        self.append_msg("Server started. Waiting for client...\n")

        self.client_socket, self.addr = self.server.accept()
        self.append_msg(f"Client connected: {self.addr}\n")

        threading.Thread(target=self.receive_msg, daemon=True).start()

    def append_msg(self, msg):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, msg)
        self.text_area.yview(tk.END)
        self.text_area.config(state=tk.DISABLED)

    def send_msg(self, event=None):
        msg = self.msg_entry.get()
        if msg:
            try:
                self.client_socket.send(msg.encode())
                self.append_msg(f"Server: {msg}\n")
                self.msg_entry.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Client disconnected")

    def receive_msg(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                if msg:
                    self.append_msg(f"Client: {msg}\n")
            except:
                self.append_msg("Client disconnected.\n")
                break

# Run the server GUI
root = tk.Tk()
app = ChatServer(root)
root.mainloop()
