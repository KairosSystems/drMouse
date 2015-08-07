#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Positr0nix"


from py2neo import authenticate, Graph



class Dbneo4j:
	
	# Realizar la conexin 
	def __init__(self, host, user, password ):
		authenticate(host,user,password)
		self.graph = Graph()

	
	def query(self, myquery ):
		return self.graph.cypher.execute( myquery )
		#nodes = graph.cypher.execute("match( (a:Sintoma)-[:ES_SINTOMA_DE]->(b:Enfermedad)) return a,b")

	def decode(self, data):
		return [  (record.name).encode('utf-8')   for record in data ]
	
	# Obtener todos los sintomas en la db	
	def getAllSintomas( self ):
		sintomas = self.query("MATCH( a:Sintoma ) RETURN a.name as name;")	
		return self.decode( sintomas )
	
	# Obtener todas las enfermedades en la db
	def getAllEnfermedades( self ):
		enfermedades = self.query("MATCH( b:Enfermedad ) RETURN b.name as name ;")
		return self.decode( enfermedades )

	
	def getEnfermedadesPorSintoma(self, sintoma ):
		query = "MATCH (a:Sintoma)-[:ES_SINTOMA_DE]->(b:Enfermedad) where a.name=\""+sintoma+"\" RETURN DISTINCT b.name as name;"
		return self.decode( self.query( query ) )


	def getSintomasPorEnfermedades( self, enfermedades ):
		str_enf = " OR ".join( [" (b.name=\""+enf+"\") " for enf in enfermedades ] )
		operador = "  "
		if ( len(enfermedades) > 0 ):
			operador = " WHERE "
		query = "MATCH( (a:Sintoma)-[:ES_SINTOMA_DE]->(b:Enfermedad) )"+operador+str_enf+" RETURN DISTINCT a.name as name;"
		return self.decode( self.query( query ) )

	def getTexto(self, enfemermedad ):
		query = "match( a:Enfermedad {name: \""+enfemermedad+"\"} ) return a.text as name;"
		record = self.query(query)
		return self.decode(record)#(record).encode('utf-8')
