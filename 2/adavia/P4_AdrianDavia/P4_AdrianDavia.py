#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sqlite3

#PASAMOS LOS DATOS A LA VENTANA DE DIALOGO
def aceptar_registro(button):
	window2.show_all()
	resultado_usuario.set_text(usuario.get_text())
	resultado_password.set_text(password.get_text())
	resultado_correo.set_text(correo.get_text())
	resultado_nombre.set_text(nombre.get_text())
	resultado_apellido.set_text(apellido.get_text())
	resultado_direccion.set_text(direccion.get_text())
	
#DEJAMOS EL DIALOGO EN SEGUNDO PLANO A CANCELAR
def cancelar_dialogo(button):
        dialogo = builder.get_object("dialogo")
        dialogo.hide()
        
#PASAMOS LOS DATOS A LA BASE DE DATOS AL DARLE A ACEPTAR        
def aceptar_dialogo(button):
        usu = resultado_usuario.get_text()
        passw = resultado_password.get_text()
        email = resultado_correo.get_text()
        name = resultado_nombre.get_text()
        lastn = resultado_apellido.get_text()
        dirc = resultado_direccion.get_text()
        cursor.execute("INSERT INTO tUsuario (Usuario,Contraseña,Email,Nombre,Apellido,Direccion)"+
                       "VALUES ('"+ usu +"','"+ passw +"','"+ email +"','"+ name +"','"+ lastn +"','"+ dirc +"')");
        conexion.commit()
        #SI PONEMOS UN PARAMETRO MAL, NO HACE INSERT
        conexion.rollback()
        
def listar(button):
        ventana2=builder.get_object("ventana_listar")
        ventana2.show_all()
    
        cursor.execute("SELECT * FROM tusuario")
        fila=cursor.fetchone()
        
        store=Gtk.ListStore(str,str,str,str,str,str)
        treeview=builder.get_object("treeview1")

        #MOSTRAMOS LOS DATOS
        for i in cursor.execute("SELECT * FROM tusuario"):
                us=str(fila[0])
                co=str(fila[1])
                em=str(fila[2])
                no=str(fila[3])
                ap=str(fila[4])
                di=str(fila[5])
                store.append(i)
                
        #ASI CREAMOS LAS COLUMNAS DEL TREEVIEW
        render=Gtk.CellRendererText()
        columna1=Gtk.TreeViewColumn("USUARIO",render,text=0)
        columna2=Gtk.TreeViewColumn("CONTRASEÑA",render,text=1)
        columna3=Gtk.TreeViewColumn("CORREO",render,text=2)
        columna4=Gtk.TreeViewColumn("NOMBRE",render,text=3)
        columna5=Gtk.TreeViewColumn("APELLIDO",render,text=4)
        columna6=Gtk.TreeViewColumn("DIRECCION",render,text=5)
        
        #ASIGNAMOS AL TREEVIEW Y VISUALIZAMOS
        treeview.set_model(store)
        treeview.append_column(columna1)
        treeview.append_column(columna2)
        treeview.append_column(columna3)
        treeview.append_column(columna4)
        treeview.append_column(columna5)
        treeview.append_column(columna6)
        treeview.show()
        
def cerrar_listar(button):
        listar = builder.get_object("ventana_listar")
        listar.hide()

def ventana_borrar(button):
	abrir = builder.get_object("dialogo_borrar")
	abrir.show_all()
	
def cancelar_registro(button):
	abrir = builder.get_object("dialogo_borrar")
	abrir.hide()
	
def borrar_registro(button):
	texto = builder.get_object("entrada_borrar")
	usu = texto.get_text()
	cursor.execute("DELETE FROM tusuario where usuario='"+ usu +"'")
	conexion.commit()
	conexion.rollback()
	
	cerrar = builder.get_object("dialogo_borrar")
	cerrar.hide()
	
def ocultar(button):
        listar = builder.get_object("ventana_listar")
        listar.hide()
        
builder=Gtk.Builder()
conexion=sqlite3.connect("tEjercicio")
cursor=conexion.cursor()
builder.add_from_file("P4_AdrianDavia.glade")
handlers ={
	"Terminar": Gtk.main_quit,
	"reposo": Gtk.main_quit,
	"aceptar_registro": aceptar_registro,
        "aceptar_dialogo": aceptar_dialogo,
        "cancelar_dialogo": cancelar_dialogo,
        "boton_listar": listar,
        "cerrar_listar": cerrar_listar,
        "borrar": borrar_registro,
        "cancelar": cancelar_registro,
        "dialogo_borrar": ventana_borrar,
        "aceptar": ocultar
}

builder.connect_signals(handlers)
window=builder.get_object("ventana")
window2=builder.get_object("dialogo")
usuario=builder.get_object("entrada_usuario")
password=builder.get_object("entrada_contra")

#ENCRYPTAMOS LA CONTRASEÑA
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
window.show_all()
Gtk.main()

