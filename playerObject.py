import random
import func
class player_basic:
	def __init__(self,name=''):
		self.name=name
		toroll=func.rollthedice('3d6')
		self.STR=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('3d6')
		self.CON=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('3d6')
		self.DEX=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('3d6')
		self.APP=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('3d6')
		self.POW=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('2d6+6')
		self.INT=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('2d6+6')
		self.EDU=int(toroll[toroll.find("=")+1:])
		toroll=func.rollthedice('2d6+6')
		self.SIZE=int(toroll[toroll.find("=")+1:])

	def basicINFO(self):
		msg='PlayerName : '+self.name +'\n'
		msg+='STR = '+str(self.STR)+"		"
		msg+='CON = '+str(self.CON)+"\n"
		msg+='DEX = '+str(self.DEX)+"		"
		msg+='APP = '+str(self.APP)+"\n"
		msg+='POW = '+str(self.POW)+"		"
		msg+='INT = '+str(self.INT)+"\n"
		msg+='EDU = '+str(self.EDU)+"		"
		msg+='SIZE = '+str(self.SIZE)+"\n"
		
		return msg
