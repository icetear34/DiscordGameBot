import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import pickle
import os
import re

#client = discord.Client()
client =commands.Bot(command_prefix="$")

@client.event
async def on_ready():
	game = discord.Game("with the API")
	await client.change_presence(activity=game)
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('discord.py:'+discord.__version__)
	print('------')

@client.command(name='RollDice',
                brief="擲骰 x個x面骰",
                aliases=['roll','dice','r'])
async def RollDice(ctx ,rolls:str):
	msg='('
	xdx=''
	total=0
	print(rolls)
	if rolls.find("+")!=-1:
		xdx=re.split('+',rolls)[0]
		total=int(re.split('-',rolls)[1])
	elif rolls.find("-")!=-1:
		xdx=re.split('-',rolls)[0]
		total=total-int(re.split('-',rolls)[1])
	else:
		xdx=rolls
	
	numDic=int(re.split('d',xdx)[0])
	
	dicVal=int(re.split('d',xdx)[1])
	print(str(numDic))
	
	for x in range(1,int(numDic)+1):
			num=random.randint(1,int(dicVal))
			if x ==(int(numDic)):
				msg=msg+str(num) + ")"
			else:
				msg=msg+str(num) + "+"
			total=total+num
	await ctx.send(msg +'='+str(total))
	print( msg +'='+str(total))


@client.command()
async def rt(ctx ,a):
	print('return > '+ a)
	print('------')

	await ctx.send(a)
	
@client.command()
async def sqr(ctx ,a):
	sqrnum=int(a) * int(a)
	print('return > '+ str(sqrnum))
	print('------')
	await ctx.send(sqrnum)	

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		msg='Hello!  '+ message.author.name +' AKA ' + message.author.nick
		await message.channel.send(msg)
	elif message.content.startswith('$whoamI'):
		msg='Hello  {0.author.mention}'.format(message)
		await message.channel.send(msg)
	elif message.content.startswith('$read'):
		await message.channel.send('can''t')
	elif message.content.startswith('$MAO'):
		await message.channel.send('878787')
	elif message.content.startswith('...'):
		await message.channel.send('878787')
	
	print('command >> '+ message.content)
	await client.process_commands(message)



client.run('MzUyNjYzMTA0MDc0NTQ3MjAw.DdFhoQ.dEEIHthy4D3M7ABT2QjWf9Gxi6I')
