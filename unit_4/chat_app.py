import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# ================= CHAT APP ==================
class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Chat Messenger 💬")
        self.master.geometry("600x650")
        self.master.configure(bg="#ECE5DD")
        self.conn = None
        self.role = None

        # ---------- HEADER ----------
        header = tk.Frame(master, bg="#075E54", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Python Chat Messenger", font=("Helvetica", 18, "bold"),
                 bg="#075E54", fg="white").pack(pady=10)

        # ---------- SETTINGS ----------
        top_frame = tk.Frame(master, bg="#ECE5DD")
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Mode:", bg="#ECE5DD", font=("Arial", 11, "bold")).grid(row=0, column=0)
        self.mode_var = tk.StringVar(value="server")
        ttk.Radiobutton(top_frame, text="Server", variable=self.mode_var, value="server").grid(row=0, column=1)
        ttk.Radiobutton(top_frame, text="Client", variable=self.mode_var, value="client").grid(row=0, column=2, padx=5)

        tk.Label(top_frame, text="Host:", bg="#ECE5DD").grid(row=1, column=0)
        self.host_entry = ttk.Entry(top_frame, width=15)
        self.host_entry.grid(row=1, column=1)
        self.host_entry.insert(0, "localhost")

        tk.Label(top_frame, text="Port:", bg="#ECE5DD").grid(row=1, column=2)
        self.port_entry = ttk.Entry(top_frame, width=10)
        self.port_entry.grid(row=1, column=3)
        self.port_entry.insert(0, "9999")

        ttk.Button(top_frame, text="Start Chat", command=self.start_chat).grid(row=1, column=4, padx=10)

        # ---------- CHAT AREA ----------
        chat_frame = tk.Frame(master, bg="#ECE5DD", bd=2)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.canvas = tk.Canvas(chat_frame, bg="#ECE5DD", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ECE5DD")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # ---------- MESSAGE INPUT ----------
        msg_frame = tk.Frame(master, bg="#DCF8C6")
        msg_frame.pack(fill=tk.X, padx=10, pady=8)

        self.msg_entry = tk.Text(msg_frame, height=3, font=("Arial", 11))
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        self.msg_entry.bind("<Return>", self.send_msg_event)

        ttk.Button(msg_frame, text="Send", command=self.send_msg).pack(side=tk.RIGHT, padx=5, pady=5)

        # ---------- STATUS ----------
        self.status_label = tk.Label(master, text="Not connected", bg="#ECE5DD", fg="red", font=("Arial", 10, "italic"))
        self.status_label.pack(pady=5)

    # ---------- CONNECTION SETUP ----------
    def start_chat(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        self.role = self.mode_var.get()

        if self.role == "server":
            threading.Thread(target=self.start_server, args=(host, port), daemon=True).start()
        else:
            threading.Thread(target=self.start_client, args=(host, port), daemon=True).start()

    def start_server(self, host, port):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((host, port))
            self.server.listen(1)
            self.add_message("🟢 Waiting for client...", "system")
            self.status_label.config(text="Server started", fg="green")
            self.conn, addr = self.server.accept()
            self.add_message(f"✅ Client connected: {addr}", "system")
            threading.Thread(target=self.receive_msg, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def start_client(self, host, port):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((host, port))
            self.conn = self.client
            self.add_message("🟢 Connected to server.", "system")
            self.status_label.config(text="Connected", fg="green")
            threading.Thread(target=self.receive_msg, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------- SENDING & RECEIVING ----------
    def send_msg_event(self, event):
        self.send_msg()
        return "break"  # prevent newline

    def send_msg(self):
        msg = self.msg_entry.get("1.0", tk.END).strip()
        if not msg or not self.conn:
            return
        try:
            self.conn.send(msg.encode())
            self.add_message(msg, "you")
            self.msg_entry.delete("1.0", tk.END)
        except:
            messagebox.showerror("Error", "Connection lost")

    def receive_msg(self):
        while True:
            try:
                data = self.conn.recv(1024).decode()
                if not data:
                    break
                self.add_message(data, "other")
            except:
                self.add_message("🔴 Disconnected.", "system")
                self.status_label.config(text="Disconnected", fg="red")
                break

    # ---------- DISPLAY MESSAGES ----------
    def add_message(self, msg, sender):
        bubble = tk.Frame(self.scrollable_frame, bg="#ECE5DD", pady=2)

        if sender == "you":
            lbl = tk.Label(bubble, text=msg, bg="#DCF8C6", fg="black", wraplength=350,
                           justify="left", font=("Arial", 11), padx=10, pady=6, bd=1,
                           relief="solid")
            lbl.pack(anchor="e", padx=10, pady=2)
        elif sender == "other":
            lbl = tk.Label(bubble, text=msg, bg="#FFFFFF", fg="black", wraplength=350,
                           justify="left", font=("Arial", 11), padx=10, pady=6, bd=1,
                           relief="solid")
            lbl.pack(anchor="w", padx=10, pady=2)
        else:
            lbl = tk.Label(bubble, text=msg, bg="#ECE5DD", fg="gray", font=("Arial", 10, "italic"))
            lbl.pack(anchor="center", pady=3)

        bubble.pack(fill="x", padx=5)
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

# ---------- MAIN ----------
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = ChatApp(root)
    root.mainloop()
