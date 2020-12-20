## tests
from FiltroDeBloom import *
from BitVector import *

def testEstFiltroDeBloom():
	m = 5
	k = 2
	filtro = FiltroDeBloom(m,k)
	assert len(filtro.V) == m
	assert len(filtro.semillas) == k
	assert filtro.V == BitVector(size=m)
	filtro.insertar("string") 
	assert filtro.V != BitVector(size=m)
	s = "s"
	i = 0
	while i < 20:
		filtro.insertar(s*i)
		i+=1


def testFnesFiltroDeBloom():
	m = 5
	k = 2
	filtro = FiltroDeBloom(m,k)
	filtro.insertar("hola")
	assert filtro.revisar("cachilupi") == 0
	filtro.insertar("chao")
	filtro.insertar("jiji")
	assert filtro.revisar("hola") == 1
	assert filtro.revisar("chao") == 1
	assert filtro.revisar("jiji") == 1


if __name__ == "__main__":
    testEstFiltroDeBloom()
    testFnesFiltroDeBloom()
    print("Felicitaciones, soy mateu")