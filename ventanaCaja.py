import tkinter as tk
from tkinter import ttk


class Caja(tk.Tk):
    def __init__(self):

        #Configuracion de la ventana
        super().__init__()
        self.columnconfigure(index=0, weight=3)
        self.columnconfigure(index=1, weight=3)
        self.resizable(False, False)

        #definicion y caracteristicas de los widgets de la ventana
        self.title_lb = tk.Label(self, text='En Proceso', font=('Arial', 24), anchor=tk.W)
        self.ordenes_lst = ttk.Treeview(self, columns=['content', 'price'])
        self.pedido_bt = tk.Button(self, text='Nuevo Pedido', font=('Arial', 12))
        self.entregar_bt = tk.Button(self, text='Entregar', font=('Arial', 12))
        self.eliminar_bt = tk.Button(self, text='Eliminar', font=('Arial', 12))

        self.ordenes_lst.heading('#0', text='N° Orden', anchor=tk.W)
        self.ordenes_lst.heading('content', text='Ordenado', anchor=tk.W)
        self.ordenes_lst.heading('price', text='Total', anchor=tk.W)

        self.ordenes_lst.insert("", tk.END, text='Hola', values=('200', 400))

        #Colocacion en la ventana
        self.title_lb.grid(    column=0, row=0)
        self.ordenes_lst.grid( column=0, row=1, rowspan=2, padx=5, pady=5)
        self.pedido_bt.grid(   column=1, row=3, ipadx=20, ipady=10, padx=5, pady=10)
        self.entregar_bt.grid( column=1, row=1, ipadx=20, ipady=10, padx=5, pady=10)
        self.eliminar_bt.grid( column=1, row=2, ipadx=20, ipady=10, padx=5, pady=15)