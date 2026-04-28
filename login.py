import tkinter as tk
import psycopg2
import hashlib

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="hospital",
        user="postgres",
        password="1234"
    )

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    user = entry_user.get()
    pwd = hash_password(entry_pass.get())

    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (user, pwd))
    result = cur.fetchone()

    if result:
        label_result.config(text="Login correcto")
    else:
        label_result.config(text="Error login")

    conn.close()

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Usuario").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Contraseña").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack()
label_result = tk.Label(root)
label_result.pack()

root.mainloop()
