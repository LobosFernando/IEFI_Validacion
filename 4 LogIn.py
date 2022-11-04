from tkinter import *
from PIL import ImageTk, Image #pip install pillow
from tkinter import messagebox
import pymysql #pip install pymysql

#----------Primer Ventana inicio-------------------------------------
def ventana_inicio(): #Creamos la primer ventana (Inicio)
	global ventana1
	ventana1=Tk()
	#-------está porción de código va a centrar mi ventana-----------
	w = 500
	h = 380
	ws = ventana1.winfo_screenwidth()
	hs = ventana1.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------------
	ventana1.title("Bienvenidos")
	ventana1.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	
	#------------------------------------------------------
	#abrimos la imagen
	imagenA = Image.open("Imágenes/net.gif")
	#cambiamos el tamaño
	resized = imagenA.resize((450, 225), Image.ANTIALIAS)
	imagenA = ImageTk.PhotoImage(resized)
	label=Label(ventana1,image=imagenA).place(x=20,y=10)
	#-----------------------------------------------------
	
	#https://wiki.tcl-lang.org/page/Colors+with+Names fuentes de colores                
	Button(ventana1,text="Iniciar Sesión", height="1", width="30",bg="navy", fg="white", font=("Calibri", 15), command=ventana_login).place(x=100,y=270)
	Button(ventana1,text="Registrar Administrador", height="1", width="30",bg="navy", fg="white", font=("Calibri", 15), command=ventana_registrar_admin).place(x=100,y=320)
	
	mainloop()
#--------------------------------------------------------------------

#----------Segunda Ventana Admin (Interfaz)--------------------------
def ventana_registrar_admin():
	ventana1.destroy()#indicamos que cierre la ventana principal
	global ventana2
	ventana2=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 360
	ws = ventana2.winfo_screenwidth()
	hs = ventana2.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana2.title("Registar Administrador")
	ventana2.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	
	#------------------------------------------------------
	#abrimos la imagen
	imagenB = Image.open("Imágenes/NuevoUsuario.gif")
	#cambiamos el tamaño
	resized = imagenB.resize((105, 120), Image.ANTIALIAS)
	imagenB = ImageTk.PhotoImage(resized)
	label=Label(ventana2,image=imagenB).place(x=100,y=10)
	#-----------------------------------------------------
	
	def limpiar_cajas_admin():
		usuario.set("")
		mail.set("")
		contrasena1.set("")
		contrasena2.set("")
	
	def registras_admin():
		if (usuario.get()== ""):
			entry_usuario.focus()
			messagebox.showinfo("Faltan datos","ingrese Usuario")#Importar libreria de mensajes
			return
		elif (mail.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Mail")
			entry_mail.focus()
			return
		elif (contrasena1.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Contraseña")
			entry_contrasena1.focus()
			return
		elif (contrasena2.get()== ""):
			messagebox.showinfo("Faltan datos","Repita Contraseña")
			entry_contrasena2.focus()
			return
		elif (contrasena1.get()!= contrasena2.get()):
			messagebox.showinfo("Error","Las Contraseñas no Coinciden")
			return
				
		basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa") #creamos la base de datos indicandole la ruta (ubicación)
		fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla
		
		fcursor.execute("SELECT Usuario FROM Admin  WHERE Usuario='"+ usuario.get()+"'")
				
		if fcursor.fetchall():
			messagebox.showinfo("Aviso","Usuario ya Registrado")
		else:
			sql= "INSERT INTO Admin (Usuario, Mail, Contrasena) VALUES ('{0}','{1}', '{2}')".format(usuario.get(), mail.get(), contrasena1.get())
			fcursor.execute(sql)
			basedatos.commit()
			messagebox.showinfo("Registro","Se registro el Usaurio con exito")
			
			limpiar_cajas_admin()
		basedatos.close()
	
	Label(ventana2, text="Usuario").place(x=50,y=160)
	Label(ventana2, text="Mail").place(x=50,y=200)
	Label(ventana2, text="Contraseña").place(x=50,y=240)
	Label(ventana2, text="R. Contraseña").place(x=50,y=280)
	
	usuario = StringVar()
	mail = StringVar()
	contrasena1 = StringVar()
	contrasena2 = StringVar()
	
	entry_usuario = Entry(ventana2,textvariable= usuario)
	entry_usuario.pack()
	entry_usuario.place(x=140,y=160)
	
	entry_mail = Entry(ventana2,textvariable= mail)
	entry_mail.pack()
	entry_mail.place(x=140,y=200)
	
	entry_contrasena1 = Entry(ventana2,textvariable=contrasena1, show="*")
	entry_contrasena1.pack()
	entry_contrasena1.place(x=140,y=240)
	
	entry_contrasena2 =Entry(ventana2,textvariable=contrasena2, show="*")
	entry_contrasena2.pack()
	entry_contrasena2.place(x=140,y=280)
	
	Button(ventana2,text="Guardar", width="10", command=registras_admin,bg="green", fg="white").place(x=18,y=320)
	Button(ventana2,text="Cancelar",width="10", command=(),bg="red", fg="white").place(x=108,y=320)
	Button(ventana2,text="Salir", width="10", command=volver_inicio,bg="navy", fg="white").place(x=198,y=320)
	
	mainloop()
#--------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
def ventana_login(): #Creamos la tercer ventana 3 (login) 
	ventana1.destroy()#indicamos que cierre la ventana principal
	global ventana3
	ventana3=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 300
	ws = ventana3.winfo_screenwidth()
	hs = ventana3.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana3.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana3.title("Registar Usuario")
	ventana3.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	
	#------------------------------------------------------
	#abrimos la imagen
	imagen = Image.open("Imágenes/login.png")
	#cambiamos el tamaño
	resized = imagen.resize((105, 120), Image.ANTIALIAS)
	imagen = ImageTk.PhotoImage(resized)
	label=Label(ventana3,image=imagen).place(x=100,y=10)
	#-----------------------------------------------------
	
	def limpiar_cajas2(): #Limpiar cajas login
		usuarioL.set("")
		contrasenaL.set("")

	def validar_admin(): #Validar usuario login 
		if (usuarioL.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Usuario")
			entry_usuario.focus()
		elif (contrasenaL.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Contraseña")
			entry_contrasena.focus()
			return
			
		basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa") #creamos la base de datos indicandole la ruta (ubicación)
		fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla
			
		fcursor.execute("SELECT Usuario FROM Admin WHERE Usuario='"+ usuarioL.get()+"' and Contrasena='"+contrasenaL.get()+"'")
				
		if fcursor.fetchall():
			messagebox.showinfo("Inicio","Bienvenido al sistema")
		else:
			messagebox.showinfo("Error","Usuario/Contraseña incorrecto")
		basedatos.close()
	
	global usuarioL, contrasenaL
	usuarioL = StringVar()
	contrasenaL = StringVar()
	
	Label(ventana3, text="Usuario").place(x=50,y=160)
	Label(ventana3, text="Contraseña").place(x=50,y=200)

	entry_usuario = Entry(ventana3,textvariable= usuarioL)
	entry_usuario.pack()
	entry_usuario.place(x=140,y=160)
	
	entry_contrasena = Entry(ventana3,textvariable= contrasenaL,  show="*")
	entry_contrasena.pack()
	entry_contrasena.place(x=140,y=200)
	
	Button(ventana3,text="Entrar", width="15", command=validar_admin,bg="green", fg="white").place(x=25,y=250)
	Button(ventana3,text="Salir", width="15", command=volver_inicio2,bg="navy", fg="white").place(x=160,y=250)
	
	mainloop()	
#-------------------------------------------------------------------------------------------

#---------------Funciones para volver a otras ventanas----------------
def volver_inicio(): #volver a inicio desde registar administrador
	ventana2.destroy() #destruimos ventana 2
	ventana_inicio() # volvemos a crear ventana 1 llamando a la función

def volver_inicio2(): #volver a inicio desde login 
	ventana3.destroy() #destruimos ventana 3
	ventana_inicio() # volvemos a crear ventana 1 llamando a la función
#--------------------------------------------------------------------
ventana_inicio()

