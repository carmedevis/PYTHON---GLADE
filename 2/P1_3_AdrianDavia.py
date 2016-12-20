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
        dialogo = builder.get_object("dialogo")
        dialogo.hide()
        
#Al pulsar el botón aceptar, introducimos los datos en la base de datos        
def aceptar_dialogo(button):
        usu = resultado_usuario.get_text()
        pasw = resultado_password.get_text()
        corr = resultado_correo.get_text()
        name = resultado_nombre.get_text()
        apell = resultado_apellido.get_text()
        dircc =resultado_direccion.get_text()

        cursor.execute("INSERT INTO tUsuario (Usuario,Contrasenya,Email,Nombre,Apellido,Direccion)"+
"VALUES ('"+usu+"','"+pasw+"','"+corr+"','"+name+"','"+apell+"','"+dircc+"')");	

        conec.commit()
        conec.rollback()
        conec.close()

#Al pulsar el botón listar, aparecen los datos que están guardados en la base de datos en las etiquetas utilizadas
def listar(button):
        ventana2=builder.get_object("ventana_listar")
        cursor.execute("SELECT * FROM tusuario")
        lista0=[]
        lista1=[]
        lista2=[]
        lista3=[]
        lista4=[]
        lista5=[]
        for row in cursor:
                lista0.append(row[0])
                lista1.append(row[1])
                lista2.append(row[2])
                lista3.append(row[3])
                lista4.append(row[4])
                lista5.append(row[5])
		
                lista_usuario.set_text(str(lista0))
                lista_contrasenya.set_text(str(lista1))
                lista_correo.set_text(str(lista2))
                lista_nombre.set_text(str(lista3))
                lista_apellido.set_text(str(lista4))
                lista_direccion.set_text(str(lista5))
	
        conec.commit()
        ventana2.show()
        
        
builder = Gtk.Builder()
#Creamos la conexión a la base de datos y el cursor para movernos por ella
conec = sqlite3.connect("basededatos")
cursor = conec.cursor()
builder.add_from_file("P1_3_AdrianDavia.glade")

handlers = {
	"Terminar": Gtk.main_quit,
	"reposo":Gtk.main_quit,
	"aceptar_registro": aceptar_registro,
        "aceptar_dialogo":aceptar_dialogo,
        "cancelar_dialogo":cancelar_dialogo,
        "boton_listar": listar
}

builder.connect_signals(handlers)

window = builder.get_object("ventana")
window2 = builder.get_object("dialogo")

usuario = builder.get_object("entrada_usuario")
password = builder.get_object("entrada_contra")

password.set_visibility(False)
correo = builder.get_object("entrada_correo")
nombre = builder.get_object("entrada_nombre")
apellido = builder.get_object("entrada_apellido")
direccion = builder.get_object("entrada_direccion")

resultado_usuario = builder.get_object("etiqueta_resultado_usuario")
resultado_password = builder.get_object("etiqueta_resultado_contr")
resultado_correo = builder.get_object("etiqueta_resultado_correo")
resultado_nombre = builder.get_object("etiqueta_resultado_nombre")
resultado_apellido = builder.get_object("etiqueta_resultado_apellido")
resultado_direccion = builder.get_object("etiqueta_resultado_direccion")

lista_usuario = builder.get_object("lista_us")
lista_contrasenya = builder.get_object("lista_co")
lista_correo = builder.get_object("lista_em")
lista_nombre = builder.get_object("lista_no")
lista_apellido = builder.get_object("lista_ap")
lista_direccion = builder.get_object("lista_di")

window.show_all()

Gtk.main()

