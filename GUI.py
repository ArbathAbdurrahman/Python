#Graphical User Interface more info ada di docs.python.org dan pypi.org
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

#merubah GUI
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("pesan")

#manambahkan frame
input_frame = ttk.Frame(window)

NAMDEP = tk.StringVar()
NAMBEL = tk.StringVar()

#penempatan Grid, pack, place
input_frame.pack(padx=10,fill="x",expand=True)

#komponen
#label
nama_depan = ttk.Label(input_frame,text="nama depan")
nama_depan.pack(padx=10,fill="x",expand=True)
#entry
nama_entry = ttk.Entry(input_frame,textvariable=NAMDEP)
nama_entry.pack(padx=10,fill="x",expand=True)

#label
nama_belakang = ttk.Label(input_frame,text="nama belakang")
nama_belakang.pack(padx=10,fill="x",expand=True)
#entry
namabel_entry = ttk.Entry(input_frame,textvariable=NAMBEL)
namabel_entry.pack(padx=10,fill="x",expand=True)

#tombol
def click():
    info = f"Selamat datang {NAMDEP.get()} {NAMBEL.get()}-sama"
    showinfo(title="pesan",message=info)

tombol = ttk.Button(input_frame,text="sapa",command=click)
tombol.pack(fill='x',expand=True,padx=10,pady=10)

#loop agar tampil
window.mainloop() # untuk menampilkan ke layar