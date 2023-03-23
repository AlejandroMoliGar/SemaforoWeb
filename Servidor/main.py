from flask import Flask 
from flask import jsonify as json

app= Flask(__name__)


#Get Usuarios
@app.route("/Usarios")
def GetUsario():
    response = {'message': 'success'}
    return json(response)

#Nuebo Usuarios
@app.route("/Usarios/Nuebo")
def NueboUsario():
    response = {'message': 'success'}
    return json(response)


#Eliminar Usuarios
@app.route("/Usarios/Eliminar/<id>")
def EliminarUsario():
    response = {'message': 'success'}
    return json(response)

#Actualisar Usuarios
@app.route("/Usarios/Actualisar/<id>")
def ActualisarUsario():
    response = {'message': 'success'}
    return json(response)



#Iniciar secion
@app.route("/LogIn","POST")
def LogIn():
    response = {'message': 'success'}
    return json(response)

#Cerar Secion
@app.route("/LogOut","POST")
def LogOut():
    response = {'message': 'success'}
    return json(response)

#Lista de semaforos
@app.route("/Semaforos")
def Get():
    return json({"lista":"todos"})

#Cambiar semaforo a verde 
@app.route("/Semaforo/V/<id>","POST")
def CambiarAVerde ():
    return json({"lista":"todos"})

#Cambiar semaforo a Rojo 
@app.route("/Semaforo/R/<id>","POST")
def CambiarARojo ():
    return json({"lista":"todos"})

#Ver el estado del Semaforo 
@app.route("/Semaforo/E/<id>")
def VerEstado   ():
    return json({"lista":"todos"})

#Semaforo Ena Automatico 
@app.route("/Semaforo/A/<SetPoint>/<id>","POST")
def Automatico ():
    return json({"lista":"todos"})

#Semaforo Ena Manual 
@app.route("/Semaforo/M/<SetPoint>/<id>","POST")
def Manual ():
    return json({"lista":"todos"})


if __name__ == '__main__':
    app.run(debug=True,port=7000)