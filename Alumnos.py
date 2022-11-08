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
    
    
    #---Inicializamos los campos vacios y reestablecemos a vacío
    def limpiar_campos():
        Dni.set("")
        Nombre.set("")
        Apellido.set("")
    #---Mostrar Alumnos
    def mostrar_alumnos():
        basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa")
        cDatos=basedatos.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        cDatos.execute("SELECT * FROM alumnos")
        for row in cDatos:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
    
    #--- Registrar Alumnos
    def registrar_alumnos():
        if (Dni.get() == ""):
            eDni.focus()
            messagebox.showinfo("Ingresar un DNI")
            return
        elif (Nombre.get() == ""):
            eNombre.focus()
            messagebox.showinfo("Ingresar un NOMBRE")
            return
        elif (Apellido.get() == ""):
            eApellido.focus()
            messagebox.showinfo("Ingresar un APELLIDO")
            return
        
        basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa")
        cDatos=basedatos.cursor()
        
        cDatos.execute("SELECT DNI FROM alumnos WHERE DNI='"+ Dni.get()+"'")
        
        if cDatos.fetchall():
            messagebox.showinfo("Aviso","DNI registrado")
        else:
            sql= "INSERT INTO Alumnos (Dni, Nombre, Apellido) VALUES ('{0}','{1}', '{2}')".format(eDni.get(), eNombre.get(), eApellido.get())
            cDatos.execute(sql)
            basedatos.commit()
            messagebox.showinfo("Registro", "Registro Exitoso")
            limpiar_campos()
            mostrar_alumnos()
        basedatos.close()
    
    #---Eliminar Alumnos
    def eliminar_alumnos():
        basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa")
        cDatos=basedatos.cursor()
        cDatos.execute("DELETE FROM alumnos WHERE IdAlumnos="+IdAlumno.get())
        basedatos.commit()
        limpiar_campos()
        mostrar_alumnos()
    
    #---Modificar Alumnos
    def modificar_alumnos():
        basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa")
        cDatos=basedatos.cursor()
        datos=Dni.get(),Nombre.get(),Apellido.get()
        cDatos.execute("UPDATE alumnos SET DNI=%s, Nombre=%s, Apellido=%s WHERE IdAlumnos="+IdAlumno.get(),datos)
        basedatos.commit()
        limpiar_campos()
        mostrar_alumnos()
    #---Entrada Datos y Cajas de texto
    e1=Entry(Alumnos, textvariable=IdAlumno)
    
    entryWidht=20
    lDni=Label(Alumnos, text="DNI:", height=2)
    lDni.place(x=15, y=80)
    eDni=Entry(Alumnos, textvariable=Dni, width=entryWidht)
    eDni.place(x=45, y=85)
    
    lNombre=Label(Alumnos, text="NOMBRE:", height=2)
    lNombre.place(x=180, y=80)
    eNombre=Entry(Alumnos, textvariable=Nombre, width=entryWidht)
    eNombre.place(x=240, y=85)
    
    lApellido=Label(Alumnos, text="APELLIDO:", height=2)
    lApellido.place(x=380, y=80)
    eApellido=Entry(Alumnos, textvariable=Apellido, width=entryWidht)
    eApellido.place(x=445, y=85)
    
    #---Treeview
    tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
    tree.place(x=15, y=150)
    tree.column('#0', width=120, anchor=CENTER)
    tree.heading('#0', text="IdAlumno", anchor=CENTER)
    tree.column('#1',width=150, anchor=CENTER)
    tree.heading('#1', text="DNI", anchor=CENTER)
    tree.column('#2',width=150, anchor=CENTER)
    tree.heading('#2', text="NOMBRE", anchor=CENTER)
    tree.column('#3', width=150, anchor=CENTER)
    tree.heading('#3', text="APELLIDO", anchor=CENTER)
    #---Permite seleccionar toda una fila en el Treeview
    def seleccionarUsandoClick(event):
        item=tree.identify('item',event.x,event.y)
        IdAlumno.set(tree.item(item,"text"))
        Dni.set(tree.item(item,"values")[0])
        Nombre.set(tree.item(item,"values")[1])
        Apellido.set(tree.item(item,"values")[2])
    #---Tree Bind ERROR EN TABULACIONES
    tree.bind("<Double-1>", seleccionarUsandoClick)
    
    #---Botones
    tamWidth=15
    b1=Button(Alumnos, text="Crear Alumno", height=2, width=tamWidth, bg="green", command=registrar_alumnos)
    b1.place(relx=0.025, y=20)
    b2=Button(Alumnos, text="Modificar Alumno", height=2, width=tamWidth, bg="cyan", command=modificar_alumnos)
    b2.place(relx=0.275, y=20)
    b3=Button(Alumnos, text="Eliminar Alumno", height=2, width=tamWidth, bg="red",command=eliminar_alumnos)
    b3.place(relx=0.525, y=20)
    b4=Button(Alumnos, text="Mostrar Alumnos", height=2, width=tamWidth, bg="pink", command=mostrar_alumnos)
    b4.place(relx=0.775, y=20)
    
    mainloop()
   
Alumnos_Sistema()
