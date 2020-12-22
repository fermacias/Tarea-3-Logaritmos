import string
import random
import FiltroDeBloom


def generateRandomUser():
    length = random.randint(5, 12)
    userName = ''.join(random.choice(string.ascii_uppercase +
                                     string.ascii_lowercase + string.digits) for _ in range(length))
    return userName


def generateRandomMail():
    lengthName = random.randint(5, 8)
    user = ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(lengthName))
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    dotsomething = ''.join(random.choice(string.ascii_lowercase)
                           for _ in range(3))
    return (user + "@" + domain + "." + dotsomething)


def generarCondicionesUnExperimento(n, m, k):
    f = open("L.txt", "w")
    filtroBloom = FiltroDeBloom.FiltroDeBloom(m, k)
    usersConfirmados = []
    for i in range(n):
        user = generateRandomUser()
        mail = generateRandomMail()
        filtroBloom.insertar(user)
        f.write(user+" "+mail+"\n")
        if (i % 3 == 0):
            usersConfirmados.append(user)
    f.close()
    return filtroBloom, usersConfirmados
