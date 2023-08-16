import tkinter as tk
from ventanaCaja import Caja


def main():
    mainScreen = tk.Tk()
    mainScreen.resizable(False, False)

    #Set up del menu principal
    mainFrame = tk.Frame(mainScreen, background='red')

    welcome_lb = tk.Label(mainFrame, text='Powitanie', font=('Blackadder ITC', 48), background='red')
    nuevaCaja_bt = tk.Button(mainFrame, bg='coral4', activebackground='coral',text='Nueva Caja', font=('Arial', 14), command=nuevaCaja_bt_event)
    cambMenu_bt = tk.Button(mainFrame, bg='coral4', activebackground='coral', text='Administrar Menu', font=('Arial', 14), command=cambMenu_bt_event)
    resumen_bt = tk.Button(mainFrame, bg='coral4', activebackground='coral', text='Resumenes', font=('Arial', 14))

    mainFrame.pack(ipadx=50)
    welcome_lb.pack(side='top')
    nuevaCaja_bt.pack(pady=20, ipadx=80, ipady=20)
    cambMenu_bt.pack(pady=20, ipadx=80, ipady=20)
    resumen_bt.pack(pady=20, ipadx=80, ipady=20)


    #bucle principal
    mainScreen.mainloop()

def nuevaCaja_bt_event():
    nueva = Caja()
    nueva.mainloop()

def cambMenu_bt_event():
    pass
    #TO DO:
    #inicializar una instancia de una clase Formulario y diseñar una GUI para cambiar la DB del menu
    #Al finalizar volverá a este principal


if __name__ == '__main__':
    main()