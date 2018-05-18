import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import config ##TOKEN位置
import func ##自訂函數
import playerObject ##腳色物件
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
async def roll_dice(ctx ,rolls:str):
	msg=func.rollthedice(rolls)
	await ctx.send(msg )
	print( msg )

@client.command(name='newplayer',
                brief="建立角色",
                aliases=['np'])
async def new_player(ctx ,name:str):
	newplay = playerObject.player_basic(name)
	print(newplay.basicINFO())
	await ctx.send(newplay.basicINFO())

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



client.run(config.my_token())
