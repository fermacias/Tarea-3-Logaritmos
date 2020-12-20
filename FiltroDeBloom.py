from BitVector import *
import mmh3

## falta asegurarse de que las funciones de hash esten en el rango [0, m-1]

class FiltroDeBloom(object):

	def __init__(self, m, k):
		self.m = m
		self.k = k
		self.V = BitVector(size = m)
		self.semillas = [] ## de tamaño k
		self.initSemillas()
		

	def initSemillas():
		r = 3*self.k ## rango para escoger semillas
		i = 0
		while i < k:
			self.semillas += [random.randrange(r)] 


	def insertar(self, p):
		for sem in self.semillas:
			hp = mmh3.hash(p, sem)
			self.V[hp] = 1


	def revisar(self, p):
		for sem in self.semillas:
			hp = mmh3.hash(p, sem)
			if self.V[hp] == 0:
				return 0
		return 1




