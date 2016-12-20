#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sqlite3 as lite

def limpiar_registros(widgets):
    campoUsuario.set_text("")
    campoPassword.set_text("")
    campoCorreo.set_text("")
    campoNombre.set_text("")
    campoApellido.set_text("")
    campoDireccion.set_text("")

def guardar_registro(button):
    if campoUsuario.get_text() == "" or campoPassword.get_text() == "" or campoCorreo.get_text() == "" or campoNombre.get_text() == "" or campoApellido.get_text()=="" or campoDireccion.get_text()=="":
        dialogoMensajeCamposVacios.show_all()
    else:
        try:
            usuarioARegistrar = str(campoUsuario.get_text())
            cursor.execute('SELECT * FROM tablaUsuarios')
            fila = cursor.fetchone()
            while True:
                if fila:
                    usu = str(fila[1])
                    if usu == usuarioARegistrar:
                        dialogoMensajeUsuarioYaRegistrado.show_all()
                        fila = None
                        break
                    else:
                        fila = cursor.fetchone()
                else:
                    windowDialogoGuardarDatos.show_all()
                    resultado_usuario.set_text(campoUsuario.get_text())
                    resultado_password.set_text(campoPassword.get_text())
                    resultado_correo.set_text(campoCorreo.get_text())
                    resultado_nombre.set_text(campoNombre.get_text())
                    resultado_apellido.set_text(campoApellido.get_text())
                    resultado_direccion.set_text(campoDireccion.get_text())
                    break
            conexion.commit()
        except lite.Error, e:
            conexion.rollback()
            dialogoMensajeError.show_all()


def listar_registro(button):
    windowDialogoListarDatos.show_all()

    cursor.execute('SELECT * FROM tablaUsuarios')
    fila = cursor.fetchone()
    columnas = treeviewDatos.get_columns()

    if len(columnas) == 6:
        print ""
    else:
        addColumnListStore("USUARIO", 0)
        addColumnListStore("CONTRASEÑA", 1)
        addColumnListStore("CORREO", 2)
        addColumnListStore("NOMBRE", 3)
        addColumnListStore("APELLIDO", 4)
        addColumnListStore("DIRECCION", 5)

    lista = Gtk.ListStore(str,str,str,str,str,str)

    while True:
        if fila:
            id = int(fila[0])
            usu = str(fila[1])
            con = str(fila[2])
            ema = str(fila[3])
            nom = str(fila[4])
            apel = str(fila[5])
            direc = str(fila[6])
            lista.append([usu,con,ema,nom,apel,direc])
            fila = cursor.fetchone()
        else:
            break

    treeviewDatos.set_model(lista)

def addColumnListStore(title,columnId):
    column = Gtk.TreeViewColumn(title,Gtk.CellRendererText(),text=columnId)
    column.set_resizable(True)
    column.set_sort_column_id(columnId)
    treeviewDatos.append_column(column)

def buttonDialogoMensajeAceptar_clicked_cb(button):
    dialogoMensajeDatosGuardados.hide()
    limpiar_registros(button)
def buttonDialogoMensajeErrorAceptar_clicked_cb(button):
    dialogoMensajeError.hide()
def buttonDialogoCamposVaciosAceptar_clicked_cb(button):
    dialogoMensajeCamposVacios.hide()
def buttonVolverListarDatos_clicked_cb(button):
    windowDialogoListarDatos.hide()
    windowPrincipal.show_all()

def buttonAceptarBorrarSeleccion_clicked_cb(button):
    try:
        usuarioFila= str(campoUsuarioAEliminar.get_text())
        query = "DELETE FROM tablaUsuarios WHERE USUARIO = '%s'" %usuarioFila.strip()
        cursor.execute(query)
        conexion.commit()
        dialogMensajeUsuarioBorrado.show_all()
    except lite.Error, e:
        conexion.rollback()
        dialogoMensajeError.show_all()
def buttonCancelarBorrarSeleccion_clicked_cb(button):
    dialogoBorrarSeleccion.hide()
def buttonBorrarFilaListarDatos_clicked_cb(button):
    treeselection = treeviewDatos.get_selection()
    if treeselection.count_selected_rows()<1:
        dialogoMensajeFilaNoSeleccionada.show_all()
    else:
        dialogoBorrarSeleccion.show_all()
        (modeloFila, iterFila) = treeselection.get_selected()
        usuarioFila = modeloFila.get_value(iterFila, 0)
        campoUsuarioAEliminar.set_text(usuarioFila)

def buttonAceptarDialogoUsuarioBorrado_clicked_cb(button):
    dialogMensajeUsuarioBorrado.hide()
    dialogoBorrarSeleccion.hide()
    windowDialogoListarDatos.hide()
def buttonAceptarMensajeFilaNoSeleccionada_clicked_cb(button):
    dialogoMensajeFilaNoSeleccionada.hide()
def buttonAceptarMensajeUsuarioYaRegistrado_clicked_cb(button):
    dialogoMensajeUsuarioYaRegistrado.hide()
    campoUsuario.set_text("")

def imagemenuitemArchivoSalir_activate_cb(menuitem):
    windowPrincipal.destroy()
def imagemenuitemAcercaDe_activate_item_cb(menuitem):
    dialogoAcercaDe.show_all()
def buttonAceptarAcercaDe_clicked_cb(menuitem):
    dialogoAcercaDe.hide()

# INICIO - METODOS DEL DIALOGO
def cancelar_dialogo(button):
    windowDialogoGuardarDatos.hide()


def aceptar_dialogo(button):
    u = resultado_usuario.get_text()
    c = resultado_password.get_text()
    e = resultado_correo.get_text()
    n = resultado_nombre.get_text()
    a = resultado_apellido.get_text()
    d = resultado_direccion.get_text()

    registro = (u,c,e,n,a,d)
    try:
        cursor.execute('INSERT INTO tablaUsuarios (USUARIO,CONTRASEÑA,CORREO,NOMBRE,APELLIDO,DIRECCION) VALUES (?,?,?,?,?,?)',(registro))
        conexion.commit()
        dialogoMensajeDatosGuardados.show_all()
    except lite.Error, e:
        conexion.rollback()
        dialogoMensajeError.show_all()
    windowDialogoGuardarDatos.hide()


# FIN - METODOS DEL DIALOGO

builder=Gtk.Builder()
builder.add_from_file("P1_4_JorgeCoello.glade")

#ABRIMOS CONEXION
nombreDatabase = "Tejercicio"
conexion = None
conexion = lite.connect(nombreDatabase)
cursor = conexion.cursor()

#INDICAMOS LOS EVENTOS Y LOS RELACIONAMOS
handlers ={
	"Terminar": Gtk.main_quit,
	"reposo":Gtk.main_quit,
	"guardar_registro": guardar_registro,
	"listar_registro": listar_registro,
    "limpiar_registros": limpiar_registros,
    "buttonDialogoMensajeAceptar_clicked_cb":buttonDialogoMensajeAceptar_clicked_cb,
    "buttonDialogoMensajeErrorAceptar_clicked_cb":buttonDialogoMensajeErrorAceptar_clicked_cb,
    "buttonDialogoCamposVaciosAceptar_clicked_cb":buttonDialogoCamposVaciosAceptar_clicked_cb,
    "buttonVolverListarDatos_clicked_cb":buttonVolverListarDatos_clicked_cb,
    "buttonAceptarBorrarSeleccion_clicked_cb":buttonAceptarBorrarSeleccion_clicked_cb,
    "buttonBorrarFilaListarDatos_clicked_cb":buttonBorrarFilaListarDatos_clicked_cb,
    "buttonCancelarBorrarSeleccion_clicked_cb":buttonCancelarBorrarSeleccion_clicked_cb,
    "buttonAceptarDialogoUsuarioBorrado_clicked_cb":buttonAceptarDialogoUsuarioBorrado_clicked_cb,
    "buttonAceptarMensajeFilaNoSeleccionada_clicked_cb":buttonAceptarMensajeFilaNoSeleccionada_clicked_cb,
    "buttonAceptarMensajeUsuarioYaRegistrado_clicked_cb":buttonAceptarMensajeUsuarioYaRegistrado_clicked_cb,
    "imagemenuitemAcercaDe_activate_item_cb":imagemenuitemAcercaDe_activate_item_cb,
    "buttonAceptarAcercaDe_clicked_cb":buttonAceptarAcercaDe_clicked_cb,
    "imagemenuitemArchivoSalir_activate_cb":imagemenuitemArchivoSalir_activate_cb,
        "aceptar_dialogo":aceptar_dialogo,
        "cancelar_dialogo":cancelar_dialogo
}
#CONECTAMOS LOS EVENTOS
builder.connect_signals(handlers)

#CREAMOS LAS VARIABLES DE LOS OBJETOS QUE NECESITAMOS
windowPrincipal=builder.get_object("ventana")

campoUsuario=builder.get_object("entrada_usuario")

campoPassword=builder.get_object("entrada_contra")
campoPassword.set_visibility(False) #PARA QUE NO SE VEA LA CONTRASEÑA INTRODUCIDA

campoCorreo=builder.get_object("entrada_correo")
campoNombre=builder.get_object("entrada_nombre")
campoApellido=builder.get_object("entrada_apellido")
campoDireccion=builder.get_object("entrada_direccion")

campoUsuarioAEliminar = builder.get_object("entryUsuarioABorrar")

resultado_usuario=builder.get_object("etiqueta_resultado_usuario")
resultado_password=builder.get_object("etiqueta_resultado_contr")
resultado_correo=builder.get_object("etiqueta_resultado_correo")
resultado_nombre=builder.get_object("etiqueta_resultado_nombre")
resultado_apellido=builder.get_object("etiqueta_resultado_apellido")
resultado_direccion=builder.get_object("etiqueta_resultado_direccion")
treeviewDatos = builder.get_object("treeviewDatos")
treeviewDatos.get_selection().set_mode(Gtk.SelectionMode.SINGLE)
#DIALOGOS
dialogoMensajeFilaNoSeleccionada = builder.get_object("dialogoMensajeFilaNoSeleccionada")
dialogoMensajeDatosGuardados = builder.get_object("dialogoMensajeDatosGuardados")
windowDialogoListarDatos = builder.get_object("dialogoListarDatos")
dialogoMensajeError = builder.get_object("dialogoMensajeError")
dialogoMensajeCamposVacios = builder.get_object("dialogoMensajeCamposVacios")
dialogoBorrarSeleccion = builder.get_object("dialogoBorrarSeleccion")
dialogoMensajeUsuarioYaRegistrado = builder.get_object("dialogoMensajeUsuarioYaRegistrado")
dialogMensajeUsuarioBorrado = builder.get_object("dialogMensajeUsuarioBorrado")
windowDialogoGuardarDatos = builder.get_object("dialogoGuardarDatos")
dialogoAcercaDe = builder.get_object("dialogoAcercaDe")
#MOSTRAMOS LA VENTANA PRINICPAL
windowPrincipal.show_all()

#MOSTRAMOS EL MAIN
Gtk.main()

