from urllib.request import urlopen
import appProyecto.models as m
import json
from appProyecto import app, db
from flask import jsonify

#CARGANDO EMPRESAS

with open('../empresas.json') as json_file:
    data = json.load(json_file)

arrayBuffer = []
for empresas in data:
    new_entry = m.Empresa(nombre=empresas['nombre'],
                        ciudad=empresas['ciudad'],
                        mail=empresas['mail'],
                        telefono=empresas['telefono'])
    arrayBuffer.append(new_entry)
db.session.add_all(arrayBuffer)
db.session.commit()

#CARGANDO PARTICIPANTES

with open('../participantes.json') as json_file2:
    data2 = json.load(json_file2)

arrayBuffer2 = []
for participantes in data2:
    new_entry = m.Participante(nombre=participantes['nombre'],
                        localidad=participantes['localidad'],
                        telefono=participantes['telefono'])
    arrayBuffer2.append(new_entry)
db.session.add_all(arrayBuffer2)
db.session.commit()


#CARGANDO EVENTOS

url = "https://datosabiertos.ayto-arganda.es/dataset/422ba3d6-93fb-49c1-8d0c-785fd6dfb631/resource/54c98ef5-60bf-4860-822a-b02b6748535b/download/eventos-febrero.json"

# Guarda la respuesta de la url
try:
    response = urlopen(url)
except:
     print("Error 879: Never Connected")

# Guarda el json response en data
data_json = json.loads(response.read())
  
#newVariableForJsonData = jsonify("{ 'Eventos': "+data_json+"}")

# Imprime json data
arrayBuffer = []
for events in data_json:
    new_entry = m.Evento(mes=events['MES'],
                        ano=events['ANO'],
                        instalacion=events['INSTALACION'],
                        empresaId=m.Empresa.getIDbyNombre(events['ENTIDAD']),
                        actividad=events['ACTIVIDAD'],
                        deporte=events['DEPORTE'])
    arrayBuffer.append(new_entry)

db.session.add_all(arrayBuffer)
db.session.commit()
print("Done")
