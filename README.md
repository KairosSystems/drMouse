## Acerca

Pequeño programa para diagnosticar enfermedades respiratorias, utilizando la base de datos Neo4j

## Mejoras

- Se puede hacer más grande la red
- Las consultas se pueden hacer más elegantes
- Se pueden insertar propiedades en los nodos para hacer inteligente el sistema
- Se puede expandir a diferentes tipos de enfermedades
- Se puede usar la API de wikipedia para obtener información sobre las enfermedades y sus sintomas

## Installation

	crear la base de datos con db/enfermedadesDB.cypher
	configurar(user,pass,host) config/neo4j.py

	~$ pip install 
	~$ source /venv/bin/activate
  	~$ pip -r install reqs.txt
  	~$ python server.py

## API Reference

- Neo4j: http://neo4j.com/developer/get-started
- py2neo: http://py2neo.org/2.0/
- Bottle: http://bottlepy.org/docs/dev/index.html

## License
MIT: http://rem.mit-license.org
