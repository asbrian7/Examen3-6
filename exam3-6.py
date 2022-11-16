import json
from mongodb import PyMongo
from conf import varmongo

#Realice una función que reciba el número de control del estudiante y muestre un JSON con el nombre del estudiante
#y las materias y calificación de cada materia. Por ejemplo, si prueba con el número de control: 18420100,
#el formato del JSON es el siguiente:

def consultar_materias():
    obj_PyMongo = PyMongo(varmongo)
    print(" ==consulta materias por estudiante ==")
    ctrl = input("Dame el numero de control: ")
    filtro = {'control': ctrl}
    respuesta3={}
    atributos_estudiante = {"_id": 0, "nombre": 1}
    atributos_kardex = {"_id": 0, "materia": 1, "calificacion": 1}
    #sql_materias =f"SELECT E.nombre, K.materia, K.calificacion FROM estudiantes E, kardex K WHERE E.control = K.control and E.control = '{ctrl}';"
    obj_PyMongo.conectar_mongodb()
    respuesta1 = obj_PyMongo.consulta_mongodb('estudiantes',filtro,atributos_estudiante)
    respuesta3.update(respuesta1['Materias'][0])
    respuesta2 = obj_PyMongo.consulta_mongodb('kardex',filtro,atributos_kardex)
    respuesta3.update(respuesta2)
    #print("respuesta1",respuesta1)
    #print("respuesta2", respuesta2)
    obj_PyMongo.desconectar_mongodb()
   # if respuesta1["status"] and respuesta2["status"]:
    #print("estudiante: ",respuesta1["Materias"][0]["nombre"])
    #for mat in respuesta2["Materias"]:
        #print(mat["materia"], mat["calificacion"])
    respuesta3.pop('status')
   # print(respuesta3)
    with open('materiasestudiante.json', 'w') as file:
        json.dump(respuesta3, file, indent=4)


consultar_materias()