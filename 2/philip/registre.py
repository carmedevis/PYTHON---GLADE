#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from gi.repository import Gtk
import sqlite3

def on_aceptar_clicked(button):
	us= Usuari.get_text() 
	con = Contrasenya.get_text()
	email=Correu.get_text()
	nom=Nom.get_text()
	cog=Cognom.get_text()
	dire=Direccio.get_text()

	lUsuari.set_text(us)
	lContrasenya.set_text(con)
	lCorreu.set_text(email)
	lNom.set_text(nom)
	lCognom.set_text(cog)
	lDireccio.set_text(dire)
	
	finestra2.show_all()

def on_aplicar_clicked(button):

	us= Usuari.get_text() 
	con = Contrasenya.get_text()
	email=Correu.get_text()
	nom=Nom.get_text()
	cog=Cognom.get_text()
	dire=Direccio.get_text()

	conn = sqlite3.connect('Registre.db')
	c=conn.cursor()
	print "Opened database successfully";

	c.execute("INSERT INTO registre (USER,PASSWORD,EMAIL,NAME,SUBNAME,ADDRESS)"+
		" VALUES ('"+us+"','"+con+"','"+email+"','"+nom+"','"+cog+"','"+dire+"')");

	conn.commit()
	conn.close()
	print "Records created successfully";
	
	finestra2 = builder.get_object("window2")
	finestra2.hide()

def on_cancel_clicked(button):
	finestra2 = builder.get_object("window2")
	finestra2.hide()
def on_veure_clicked(button):
	conn = sqlite3.connect('Registre.db')
	cursor=conn.execute("select * from registre");
	print("conectant a la base de dades...")
	lista0=[]
	lista1=[]
	lista2=[]
	lista3=[]
	lista4=[]
	lista5=[]
	
	#a=[]
	for row in cursor:	
		lista0.append(row[0])
		lista1.append(str(row[1]))
		lista2.append(str(row[2]))
		lista3.append(str(row[3]))
		lista4.append(str(row[4]))
		lista5.append(str(row[5]))
		
		#a=(lista0[u]+lista1[u]+lista2[u]+lista3[u]+lista4[u]+lista5[u]+"\n")	
		#a=a+a
		
		text.set_text(str(lista0))
		text2.set_text(str(lista1))
		text3.set_text(str(lista2))
		text4.set_text(str(lista3))
		text5.set_text(str(lista4))
		text6.set_text(str(lista5))

		#llista.append(lista0[u],lista1[u],lista3[u],lista4[u],lista2[u])	
  	

          

	finestra3.show_all()
	
def on_reset_clicked(button):
	Usuari.set_text(" ")
	Contrasenya.set_text(" ")
	Correu.set_text(" ")
	Nom.set_text(" ")
	Cognom.set_text(" ")
	Direccio.set_text(" ")
def on_button1_clicked(button):
	finestra3.hide()

builder = Gtk.Builder()			
builder.add_from_file("registre.glade")
handlers={
	"on_reset_clicked":on_reset_clicked,
	"on_aplicar_clicked":on_aplicar_clicked,
	"on_cancel_clicked":on_cancel_clicked,
	"on_aceptar_clicked":on_aceptar_clicked,
	"on_veure_clicked":on_veure_clicked,
	"on_button1_clicked":on_button1_clicked,
	"gtk_main_quit" : Gtk.main_quit,	
}


builder.connect_signals(handlers)
Usuari=builder.get_object("Usuari")
Contrasenya=builder.get_object("Contrasenya")
Correu=builder.get_object("Correu")
Nom=builder.get_object("Nom")
Cognom=builder.get_object("Cognom")
Direccio=builder.get_object("Direccio")

lUsuari=builder.get_object("lUsuari")
lContrasenya=builder.get_object("lContrasenya")
lCorreu=builder.get_object("lCorreu")
lNom=builder.get_object("lNom")
lCognom=builder.get_object("lCognom")
lDireccio=builder.get_object("lDireccio")

text=builder.get_object("text")
text2=builder.get_object("text2")
text3=builder.get_object("text3")
text4=builder.get_object("text4")
text5=builder.get_object("text5")
text6=builder.get_object("text6")


finestra2 = builder.get_object("window2")
finestra3 = builder.get_object("window3")

finestra = builder.get_object("window1")
finestra.show_all()

Gtk.main()
