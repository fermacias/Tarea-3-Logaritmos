import random
import string
import generacionesIniciales
import lookUsername


def generarQConsultas(Q):
    usersQueries = []
    for i in range(Q):
        usersQueries.append(generacionesIniciales.generateRandomUser())
    return usersQueries


def hacerQConsultasAlAzar(Q):
    users = generarQConsultas(Q)
    for usuario in users:
        lookUsername.lookFor(usuario)


def generarConsultasErradas(N):
    badUsers = []
    for i in range(1, N+1):
        badUsers.append(generacionesIniciales.generateRandomUser()+"!!!##")
    return badUsers


def hacerConsultaList(listaConsulta):
    for usuario in listaConsulta:
        lookUsername.lookFor(usuario)
