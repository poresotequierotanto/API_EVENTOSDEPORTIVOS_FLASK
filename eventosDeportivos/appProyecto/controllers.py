from appProyecto import app, db
import appProyecto.models as m
from flask import jsonify, request

# ==== Eventos API ==== #
@app.route('/eventos/', methods=['GET'])
def allEvents():
    events = m.Evento.query.all()
    response = jsonify([event.asdict() for event in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

@app.route('/eventos/put', methods=['POST'])
def putEventos():
    mes = request.form['mes']
    ano = request.form['ano']
    instalacion = request.form['instalacion']
    idEmpresa = request.form['idEmpresa']
    actividad = request.form['actividad']
    deporte = request.form['deporte']

    evento = m.Evento( mes, ano, instalacion, idEmpresa, actividad, deporte)
    db.session.add(evento)
    db.session.commit()
    return jsonify(evento.asdict())

@app.route('/eventos/delete', methods=['POST'])
def delEventos():
    idEvento = request.form['idEvento']
    evento = m.Evento.geteventobyId(idEvento)
    db.session.delete(evento)
    db.session.commit()
    return jsonify(True)

@app.route('/eventos/<rowid>', methods=['GET'])
def searchEventos(rowid):
    evento = m.Evento.query.filter_by(rowid=rowid).first_or_404()
    return jsonify(evento.asdict())

@app.route('/eventos/update/<rowid>', methods=['POST'])
def updateEvento(rowid):
    #Dentro del dict puedes agregar todas las columnas del registro a actualizar
    nuevomes = request.form['mes']
    nuevoano = request.form['ano'] 
    nuevoinstalacion = request.form['instalacion'] 
    nuevoempresaId = request.form['empresaId']
    nuevoactividad = request.form['actividad'] 
    nuevodeporte = request.form['deporte']

    if nuevomes == "":
        nuevomes = m.Evento.geteventobyId(rowid).mes

    if nuevoano == "":
        nuevoano = m.Evento.geteventobyId(rowid).ano
    
    if nuevoinstalacion == "":
        nuevoinstalacion = m.Evento.geteventobyId(rowid).instalacion
    
    if nuevoempresaId == "":
        nuevoempresaId = m.Evento.geteventobyId(rowid).empresaId

    if nuevoactividad == "":
        nuevoactividad = m.Evento.geteventobyId(rowid).actividad

    if nuevodeporte == "":
        nuevodeporte = m.Evento.geteventobyId(rowid).deporte

    m.Evento.query.filter_by(rowid=rowid).update(dict(mes=nuevomes, ano=nuevoano, instalacion=nuevoinstalacion,
                                         empresaId=nuevoempresaId,actividad=nuevoactividad,deporte=nuevodeporte))

    db.session.commit()
    return jsonify(True)


# ==== Empresas API ==== #

@app.route('/empresas/', methods=['GET'])
def allEmpresas():
    empresas = m.Empresa.query.all()
    response = jsonify([empresa.asdict() for empresa in empresas])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

@app.route('/empresas/put', methods=['POST'])
def putEmpresa():
    nombre = request.form['nombre']
    ciudad = request.form['ciudad']
    mail = request.form['mail']
    telefono = request.form['telefono']

    empresa = m.Empresa(nombre,ciudad,mail,telefono)
    db.session.add(empresa)
    db.session.commit()
    return jsonify(empresa.asdict())

@app.route('/empresas/delete', methods=['POST'])
def delEmpresas():
    idEmpresa= request.form['idEmpresa']
    empresa = m.Empresa.getEmpresaById(idEmpresa)
    db.session.delete(empresa)
    db.session.commit()
    return jsonify(True)

@app.route('/empresas/<rowid>', methods=['GET'])
def searchEmpresa(rowid):
    empresa = m.Empresa.query.filter_by(rowid=rowid).first_or_404()
    return jsonify(empresa.asdict())

@app.route('/empresas/update/<rowid>', methods=['POST'])
def updateEmpresa(rowid):
    #Dentro del dict puedes agregar todas las columnas del registro a actualizar
    nuevonombre = request.form['nombre']
    nuevociudad = request.form['ciudad']
    nuevomail = request.form['mail']
    nuevotelefono = request.form['telefono']

    if nuevonombre == "":
        nuevonombre = m.Empresa.getEmpresaById(rowid).nombre
    
    if nuevociudad == "":
        nuevociudad = m.Empresa.getEmpresaById(rowid).ciudad
    
    if nuevomail == "":
        nuevomail = m.Empresa.getEmpresaById(rowid).mail
    
    if nuevotelefono == "":
        nuevotelefono = m.Empresa.getEmpresaById(rowid).telefono

    empresa = m.Empresa.query.filter_by(rowid=rowid).update(dict(nombre=nuevonombre, ciudad=nuevociudad, mail=nuevomail, telefono=nuevotelefono))

    db.session.commit()
    return jsonify(True)
    

# ==== Participantes API ==== #

@app.route('/participantes/', methods=['GET'])
def allParticipantes():
    participantes = m.Participante.query.all()
    response = jsonify([participante.asdict() for participante in participantes])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

@app.route('/participantes/put', methods=['POST'])
def putParticipantes():
    nombre = request.form['nombre']
    localidad = request.form['localidad']
    telefono = request.form['telefono']

    participante = m.Participante(nombre,localidad,telefono)
    db.session.add(participante)
    db.session.commit()
    return jsonify(participante.asdict())

@app.route('/participantes/delete', methods=['POST'])
def delParticipante():
    idParticipante = request.form['idParticipante']
    participante = m.Participante.getParticipantebyId(idParticipante)
    db.session.delete(participante)
    db.session.commit()
    return jsonify(True)

@app.route('/participantes/update/<rowid>', methods=['POST'])
def updateParticipante(rowid):
    #Dentro del dict puedes agregar todas las columnas del registro a actualizar
    nuevonombre = request.form['nombre']
    nuevolocalidad = request.form['localidad']
    nuevotelefono = request.form['telefono']

    if nuevonombre == "":
        nuevonombre = m.Participante.getParticipantebyId(rowid).nombre
    
    if nuevolocalidad == "":
        nuevolocalidad = m.Participante.getParticipantebyId(rowid).localidad

    
    if nuevotelefono == "":
        nuevotelefono = m.Participante.getParticipantebyId(rowid).telefono

    m.Participante.query.filter_by(rowid=rowid).update(dict(nombre=nuevonombre, localidad=nuevolocalidad, telefono=nuevotelefono))

    db.session.commit()
    return jsonify(True)

@app.route('/participantes/<telefono>', methods=['GET'])
def searchParticipan(telefono):
    participante = m.Participante.query.filter_by(telefono=telefono).first_or_404()
    return jsonify(participante.asdict())
    

# ==== Participan API ==== #

@app.route('/participan/<idevento>', methods=['GET'])
def getParticipan(idevento):
    query_user_role = m.Participante.query.join(m.association_table).join(m.Evento).filter((m.association_table.c.id_part == m.Participante.rowid) & (idevento == m.Evento.rowid)).all()
    response = jsonify([participante.asdict() for participante in query_user_role])
    return response

@app.route('/participan/put', methods=['POST'])
def putParticipan():
    eventoid = request.form['eventoid']
    participanteid = request.form['participanteid']

    evento = m.Evento.geteventobyId(eventoid)
    participante = m.Participante.getParticipantebyId(participanteid)

    statement = m.association_table.insert().values(id_evento=evento.rowid, id_part=participante.rowid)
    db.session.execute(statement)
    db.session.commit()
    return jsonify(True)

