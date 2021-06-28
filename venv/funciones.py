import requests
import random
import datos

def llamado_API(caso):
    """
    Retorna el estado de la consulta junto con la Json obtenido
    """
    url = datos.informacion[caso]['url']
    r = requests.get(url, headers=datos.informacion[caso]["headers"], params=datos.informacion[caso]["params"])
    codigo = r.status_code
    return (r.json(), codigo)

################################################################################################
#####################     Funciones de Compración de estructura de APIs       ##################
################################################################################################

def llaves(caso):
    """
    Compraracion de las llaves que trae la API con las almacenadas. En caso de haber una diferencia retorna el valor
    que no se encuentra en la base en forma de lista.
    """
    api = llamado_API(caso)
    error = []
    if api[1] == 200:
        for i in api[0]:
            if i in datos.informacion[caso]["llaves"]:
                pass
            else:
                error.append(i)
    else:
        error.apend("Error en la respuesta. Codigo "+str(api[0]))
    return error

