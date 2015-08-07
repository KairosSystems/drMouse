#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Positr0nix"



import random

class Controller:

	def __init__(self, db):
		#self.db = Dbneo4j("localhost:7474","neo4j","root")
		self.reset( db )	


	def reset(self, db):
		self.sintomas = db.getAllSintomas()
		self.enfermedades = db.getAllEnfermedades()
		self.index = 0


	def _print(self):
		print "\n\n\nEnfermedades:", self.enfermedades
		print "Sintomas:", self.sintomas
		print "\n\n\n"


	def getEnfermedades(self):
		return self.enfermedades

	def isEmpty(self):
		if len( self.sintomas ) == 0 or len(self.enfermedades) == 0:
			return True
		return False

	def tenemosDiagnostico(self):
		if len( self.enfermedades ) == 1:
			return True
		return False

	def getDiagnostico(self, db):
		if len(self.enfermedades) == 0:
			return ("No puedo encontrar un diagnóstico", "Lo siento, no tengo la información necesaria para encontrar un diagnóstico :(")
		if self.tenemosDiagnostico():
			enf = self.enfermedades[0]
			[info] = self.getInfo(db, enf)
			return ("Posiblemente usted sufre de "+enf, info )
		return ("Algo raro sucedio", "Error en el infraestruktocho")

	def getInfo(self, db, enf):
		return db.getTexto( enf )

	def getPregunta(self):	
		self.index = random.randint( 0, len(self.sintomas)-1 )
		sintoma =  self.sintomas[ self.index ]
		return "¿ Usted ha sufrido de %s ?" % sintoma

	def setRespuesta(self, db, ans):
		sintoma = self.sintomas.pop( self.index ) # Obtener el sintoma a analizar
		
		if ans == "si":
			
			# obtener las enfermerdades sin las que se han descartado

			# Obtener todas las enfermedades relacionadas con el sintoma
			enfs = db.getEnfermedadesPorSintoma( sintoma ) 
			
			# Filtrar las enfermedades entre las que posibles y las obtenidas por sintoma ( Interseccion de conjuntos)
			self.enfermedades = list( set(enfs)&set(self.enfermedades) )

			# obtener los sintomas de las enfermedades sin las que se han descartado
			
			# Obtener todos los sintomas relacionados a la enfermedades
			sints = db.getSintomasPorEnfermedades( self.enfermedades )

			# Obtener los sintomas no preguntados y relacionados con las enfermedades
			self.sintomas  = list( set(sints)&set(self.sintomas) )

		else: # No

			#obtener todas las enfermedades relacionadas a ese sintoma
			enfs = db.getEnfermedadesPorSintoma( sintoma )			
			
			self.enfermedades = list( set(self.enfermedades)-set(enfs) )
			
			sints = db.getSintomasPorEnfermedades( self.enfermedades )
			
			self.sintomas = list( set(self.sintomas)&set(sints) )
		