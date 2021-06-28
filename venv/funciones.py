import requests
import random
import datos

# url = datos.informacion['nasa']['url']
#
# r = requests.get(url)
# codigo = r.status_code
# api = r.json()
# print(api)
# print(codigo)


def llamado_API(caso):
    url = datos.informacion[caso]['url']
    r = requests.get(url)
    codigo = r.status_code
    return (r.json(), codigo)


################################################################################################
#####################     Funciones de Compración de estructura de APIs       ##################
################################################################################################


def llaves(caso):
    """
    Compraracion de las llaves de la API
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
        error.apend(api[1])
    return error



#
# def areasID():
#     """
#     Compraracion del modelo de API de Areas_ID (toma un area de forma aleatoria suministrado por la API de areas)
#     """
#     url = apis['areas']
#     api = llamado_API(url)
#     id = random.randrange(1, (len(api[0])))
#     url = apis['areas_id']
#     url = url + api[0][id]['area-id']
#     api = llamado_API(url)
#     error = []
#     if api[1] == 200:
#
#         for x in api[0]:
#             if x in llaves_areas:
#                 pass
#             else:
#                 error.append(x)
#
#     return api[0]['area-id'], error
#
#
# def sistema():
#     """
#     Compraracion del modelo de API de Sistemas
#     """
#     url = apis['systems']
#     api = llamado_API(url)
#     error = []
#
#     if api[1] == 200:
#         id = random.randrange(1, (len(api[0])))
#         for x in api[0][id]:
#             if x in llaves_sistemas:
#                 pass
#             else:
#                 error.append(x)
#     return api[0][id]['system-name'], error
#
#
# def sistemasID():
#     """
#     Compraracion del modelo de API de Sistemas_ID (toma un sistema de forma aleatoria suministrado por la API de system)
#     """
#     url = apis['systems']
#     api = llamado_API(url)
#     id = random.randrange(1, (len(api[0])))
#     url = apis['systems_id']
#     url = url + api[0][id]['system-id']
#     error = []
#     api = llamado_API(url)
#
#     if api[1] == 200:
#         id = random.randrange(1, (len(api[0])))
#
#         for x in api[0]:
#             if x in llaves_sistemas:
#                 pass
#             else:
#                 error.append(x)
#
#     return api[0]['system-name'], error
#
#
# def aplicaciones():
#     """
#     Compraracion del modelo de API de Aplicaciones (toma una aplicacion de forma aleatoria)
#     """
#     url = apis['applications']
#     api = llamado_API(url)
#     error = []
#     if api[1] == 200:
#         id = random.randrange(1, (len(api[0])))
#
#         for x in api[0][id]:
#             if x in llaves_aplicaciones:
#                 pass
#             else:
#                 error.append(x)
#
#     return api[0][id]['application-id'], error
#
#
# def aplicacionesID():
#     """
#     Compraracion del modelo de API de Aplicaciones_ID (toma un sistema de forma aleatoria suministrado por la API de application)
#     """
#     url = apis['applications']
#     api = llamado_API(url)
#     id = random.randrange(1, (len(api[0])))
#     url = apis['applications_id']
#     url = url + api[0][id]['application-id']
#     api = llamado_API(url)
#     error = []
#
#     if api[1] == 200:
#         id = random.randrange(1, (len(api[0])))
#
#         for x in api[0][id]:
#             if x in llaves_aplicaciones:
#                 pass
#             else:
#                 error.append(x)
#
#     return api[0]['application-id'], error
#
#
# def instancias():
#     """
#     Compraracion del modelo de API de Instancias (toma una instancia de forma aleatoria)
#     """
#     url = apis['instances']
#     api = llamado_API(url)
#     error = []
#
#     if api[1] == 200:
#         for x in api[0]:
#             for i in x:
#                 if i in llaves_instancias:
#                     pass
#                 else:
#                     error.append(i+" en la instancia "+x)
#
#     return error