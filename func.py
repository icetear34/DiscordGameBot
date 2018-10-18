import random
import re


##擲骰 ex:2d6+2
def rollthedice(rolls:str):
	msg='('
	dices=''
	addmsg=''
	total=0
	print("rollthedice : "+rolls)
	if rolls.find("+")!=-1:
		dices=rolls.split('+')[0]
		total=int(rolls.split('+')[1])
		addmsg=rolls[rolls.find("+"):]
	elif rolls.find("-")!=-1:
		dices=rolls.split('-')[0]
		total=total-int(rolls.split('-')[1])
		addmsg=rolls[rolls.find("-"):]
	else:
		dices=rolls
	
	numDic=int(re.split('d',dices)[0])
	
	dicVal=int(re.split('d',dices)[1])
	
	for x in range(1,int(numDic)+1):
			num=random.randint(1,int(dicVal))
			if x ==(int(numDic)):
				msg=msg+str(num) + ")"
			else:
				msg=msg+str(num) + "+"
			total=total+num
	msg=msg+addmsg+'='+str(total)
	return msg