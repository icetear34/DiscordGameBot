import sys
sys.path
import discord
import asyncio
import config
client = discord.Client()

@ client.event 
async  def  on_ready():
     print(' Logged in ')
     print(client.user.name)
     print(client.user.id)
     print(' ------ ')

@ client.event 
async  def  on_message(message):
     if message.content.startswith('！test '):
        counter =  0 
        tmp = await client.send_message(message.channel,' Calculating messages ... ')
        async for log in client.logs_from(message.channel,limit = 100):
            if log.author == message.author:
                計數器 +=  1

        await client.edit_message(tmp,'你有{}消息。', format(counter))
     elif message.content.startswith('！sleep '):
         await asyncio.sleep(5)
         await client.send_message(message.channel,'完成睡覺')

client.run(my_token())