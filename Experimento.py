import generacionesIniciales
import Consultas
import lookUsername


def experimento(n, m, k):
    filtroBloom, usuariosCorrectos = generacionesIniciales.generarCondicionesUnExperimento(
        n, m, k)
    lookUsername.setBloomFilter(filtroBloom)
    usuariosIncorrectos = Consultas.generarConsultasErradas(n//3)
    Consultas.hacerConsultaList(usuariosCorrectos)
    Consultas.hacerConsultaList(usuariosIncorrectos)
    Consultas.hacerQConsultasAlAzar(
        n-(len(usuariosCorrectos)+len(usuariosIncorrectos)))


if __name__ == "__main__":
    experimento(100, 100, 2)
