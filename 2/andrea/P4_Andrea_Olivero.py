#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sqlite3

#Introducimos los datos del formulario en la ventana de diálogo
def aceptar_registro(button):
	window2.show_all()

	resultado_usuario.set_text(usuario.get_text())
	resultado_password.set_text(password.get_text())
	resultado_correo.set_text(correo.get_text())
	resultado_nombre.set_text(nombre.get_text())
	resultado_apellido.set_text(apellido.get_text())
	resultado_direccion.set_text(direccion.get_text())
	
#Al pulsar el botón cancelar, se queda en un segundo plano
def cancelar_dialogo(button):
        dialogo=builder.get_object("dialogo")
        dialogo.hide()
        
#Al pulsar el botón aceptar, introducimos los datos en la base de datos        
def aceptar_dialogo(button):
        u=resultado_usuario.get_text()
        p=resultado_password.get_text()
        c=resultado_correo.get_text()
        n=resultado_nombre.get_text()
        a=resultado_apellido.get_text()
        d=resultado_direccion.get_text()

        cursor.execute("INSERT INTO tUsuario (Usuario,Contrasenya,Email,Nombre,Apellido,Direccion)"+
"VALUES ('"+u+"','"+p+"','"+c+"','"+n+"','"+a+"','"+d+"')");	

        conec.commit()
        conec.rollback()

#Al pulsar el botón listar, aparecen los datos que están guardados en la base de datos en las etiquetas utilizadas
def listar(button):
        ventana=builder.get_object("ventana_listar")
        ventana.show()        
     
        cursor.execute("SELECT * FROM tusuario")
        fila=cursor.fetchone()
        
        #Definimos la lista y el objeto treeview
        store=Gtk.ListStore(str,str,str,str,str,str)
        treeview=builder.get_object("treeview")

	#Mostramos los datos y los añadimos a la lista
        for i in cursor.execute("SELECT * FROM tusuario"):
               u=str(fila[0])
               c=str(fila[1])
               e=str(fila[2])
               n=str(fila[3])
               a=str(fila[4])
               d=str(fila[5])
               store.append(i)
	
	#Creamos las columnas del treeview
        render=Gtk.CellRendererText()
        columna1=Gtk.TreeViewColumn("Usuario",render,text=0)
        columna2=Gtk.TreeViewColumn("Contrasenya",render,text=1)
        columna3=Gtk.TreeViewColumn("Email",render,text=2)
        columna4=Gtk.TreeViewColumn("Nombre",render,text=3)
        columna5=Gtk.TreeViewColumn("Apellido",render,text=4)
        columna6=Gtk.TreeViewColumn("Direccion",render,text=5)

	#Relacionamos la lista y las columnas con nuestro treeview
        treeview.set_model(store)
        treeview.append_column(columna1)
        treeview.append_column(columna2)
        treeview.append_column(columna3)
        treeview.append_column(columna4)
        treeview.append_column(columna5)
        treeview.append_column(columna6)
      
	#Mostramos el treeview
        treeview.show()

#Creamos las funciones para eliminar los registros, cerrar los dialogos y ocultarlos        
def cerrarListar(button):
        listar=builder.get_object("ventana_listar")
        listar.hide()

def ventana_borrar(button):
	abrir=builder.get_object("dialogo_borrar")
	abrir.show_all()
	
def cancelar(button):
	abrir=builder.get_object("dialogo_borrar")
	abrir.hide()
	
def borrar(button):
	texto=builder.get_object("entrada")
	u=texto.get_text()
	cursor.execute("DELETE FROM tusuario where Usuario='"+u+"'")
	conec.commit()
	conec.rollback()
	
	cerrar=builder.get_object("dialogo_borrar")
	cerrar.hide()
	
def ocultar(button):
        listar=builder.get_object("ventana_listar")
        listar.hide()

builder=Gtk.Builder()
#Creamos la conexión a la base de datos y el cursor para movernos por ella
conec=sqlite3.connect("basededatos")
cursor=conec.cursor()
#Relacionamos el fichero de glade con el de python
builder.add_from_file("P4_Andrea_Olivero.glade")

#Relacionamos los eventos del archivo glade con las funciones de python
handlers ={
	"Terminar": Gtk.main_quit,
	"reposo":Gtk.main_quit,
	"aceptar_registro": aceptar_registro,
        "aceptar_dialogo":aceptar_dialogo,
        "cancelar_dialogo":cancelar_dialogo,
        "boton_listar": listar,
        "cerrarListar": cerrarListar,
        "borrar":borrar,
        "cancelar":cancelar,
        "dialogo_borrar":ventana_borrar,
	"cerrar": ocultar
}

builder.connect_signals(handlers)

#Creamos las variables
window=builder.get_object("ventana")
window2=builder.get_object("dialogo")

usuario=builder.get_object("entrada_usuario")
password=builder.get_object("entrada_contra")

password.set_visibility(False)
correo=builder.get_object("entrada_correo")
nombre=builder.get_object("entrada_nombre")
apellido=builder.get_object("entrada_apellido")
direccion=builder.get_object("entrada_direccion")

resultado_usuario=builder.get_object("etiqueta_resultado_usuario")
resultado_password=builder.get_object("etiqueta_resultado_contr")
resultado_correo=builder.get_object("etiqueta_resultado_correo")
resultado_nombre=builder.get_object("etiqueta_resultado_nombre")
resultado_apellido=builder.get_object("etiqueta_resultado_apellido")
resultado_direccion=builder.get_object("etiqueta_resultado_direccion")


#Mostramos la ventana principal
window.show_all()

Gtk.main()

