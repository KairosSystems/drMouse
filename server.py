#!/usr/bin/python
# -*- coding: utf-8 -*-

from tools.bottle import *
from tools.controller import *
from tools.dbneo4j import *
import config.neo4j as config

# see in config/dbneo4j.py for you configuration
db = Dbneo4j( config.host, config.user, config.password )
controller = Controller(db)

def apptemplate( mytemplate ):
	return template('public/views/header')+template(mytemplate)+template('public/views/footer')

@route("/")
def index():
	global controller, db
	controller.reset( db )
	return apptemplate( template('public/views/index') )

@route("/newconsulta")
def index():
	global controller, db
	controller.reset( db )
	redirect("/consulta")

@route("/consulta")
def index():
	global controller 	
	myask = controller.getPregunta()
	enfs = controller.getEnfermedades()
	return apptemplate( template('public/views/consulta', pregunta=myask, enfermedades=enfs ) )

@route("/consulta/<ans>")
def index(ans):
	global controller, db
	controller.setRespuesta(db, ans)
	if controller.tenemosDiagnostico() or controller.isEmpty():
		redirect('/diagnostico')
	redirect('/consulta') 

@route("/enfs")
def index():
	global controller
	enfs = controller.getEnfermedades()
	return apptemplate( template('public/views/enfermedades', enfermedades=enfs) )

@route("/enfs/<name>")
def index(name):
	global controller, db
	enf = name
	[texto] = controller.getInfo(db, enf)
	sintomas = db.getSintomasPorEnfermedades( [enf] )
	return apptemplate( template('public/views/info', enfermedad=enf, texto=texto, sintomas=sintomas) )


@route("/diagnostico")
def index():
	global controller, db
	(diag, info) = controller.getDiagnostico( db )
	return apptemplate( template('public/views/diagnostico', diagnostico=diag, texto=info) )

#  for get all the assets public (dir)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='public')


debug(True)
run(host='localhost',port=8080)
