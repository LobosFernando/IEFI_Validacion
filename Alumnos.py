from tkinter import *
from PIL import ImageTk, Image #pip install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql #pip install pymysql

def Alumnos_Sistema():
    #---Inicializar Campos visuales
    global Alumnos
    Alumnos = Tk()
    #---Ventana Alumnos_Sistema
    w = 600
    h = 400
    ws = Alumnos.winfo_screenwidth()
    hs = Alumnos.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    Alumnos.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Alumnos.resizable(False, False)
    Alumnos.title("Carga de Alumnos")
    Alumnos.iconbitmap("Imágenes/Student.ico")
    #---Variables caja de texto
    IdAlumno=StringVar()
    Dni=StringVar()
    Nombre=StringVar()
    Apellido=StringVar()
    #---Botones
    tamWidth=15
    b1=Button(Alumnos, text="Crear Alumno", height=2, width=tamWidth, bg="green")
    b1.place(relx=0.025, y=20)
    b2=Button(Alumnos, text="Modificar Alumno", height=2, width=tamWidth, bg="cyan")
    b2.place(relx=0.275, y=20)
    b3=Button(Alumnos, text="Eliminar Alumno", height=2, width=tamWidth, bg="red")
    b3.place(relx=0.525, y=20)
    b4=Button(Alumnos, text="Mostrar Alumnos", height=2, width=tamWidth, bg="pink")
    b4.place(relx=0.775, y=20)
    #---Entrada Datos y Cajas de texto
    
    e1=Entry(Alumnos, textvariable=IdAlumno)
    
    entryWidht=20
    l2=Label(Alumnos, text="DNI:", height=2)
    l2.place(x=15, y=80)
    e2=Entry(Alumnos, textvariable=Dni, width=entryWidht)
    e2.place(x=45, y=85)
    
    l3=Label(Alumnos, text="NOMBRE:", height=2)
    l3.place(x=180, y=80)
    e3=Entry(Alumnos, textvariable=Nombre, width=entryWidht)
    e3.place(x=240, y=85)
    
    l4=Label(Alumnos, text="APELLIDO:", height=2)
    l4.place(x=380, y=80)
    e4=Entry(Alumnos, textvariable=Apellido, width=entryWidht)
    e4.place(x=445, y=85)
    
    #---Treeview
    tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
    tree.place(x=15, y=150)
    tree.column('#0',width=120)
    tree.heading('#0', text="IdAlumno", anchor=CENTER)
    tree.column('#1',width=150)
    tree.heading('#1', text="DNI", anchor=CENTER)
    tree.column('#2',width=150)
    tree.heading('#2', text="NOMBRE", anchor=CENTER)
    tree.column('#3', width=150)
    tree.heading('#3', text="APELLIDO", anchor=CENTER)
    #---Permite seleccionar toda una fila en el Treeview
    def seleccionarUsandoClick(event):
        item=tree.identify('item',event.x,event.y)
        IdAlumno.set(tree.item(item,"text"))
        Dni.set(tree.item(item,"values")[0])
        Nombre.set(tree.item(item,"values")[1])
        Apellido.set(tree.item(item,"values")[2])

        tree.bind("<Double-1>", seleccionarUsandoClick)

    # l2=Label(Alumnos, text="Nombre")
    # l2.place(x=60,y=10)
    # e2=Entry(Alumnos, textvariable=Nombre, width=50)
    # e2.place(x=100, y=10)

    # l3=Label(Alumnos, text="Apellido")
    # l3.place(x=50,y=40)
    # e3=Entry(Alumnos, textvariable=Apellido)
    # e3.place(x=100, y=40)

    # l4=Label(Alumnos, text="Dni")
    # l4.place(x=280,y=40)
    # e4=Entry(Alumnos, textvariable=Dni, width=10)
    # e4.place(x=320, y=40)

    
    
    mainloop()
   
Alumnos_Sistema()
