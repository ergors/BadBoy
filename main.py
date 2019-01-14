#!/usr/bin/python3
# -*- encoding: utf-8 -*_
# BadBoy Bot
# Funcionando em Python 3.6
import discord

from commands.HelpCommand import HelpCommand
from commands.framework.CommandCenter import CommandCenter

TOKEN = 'NTE5MTk3ODI2NTY0MDk2MDMw.Dwhy1w.SI3U2z9Y5tX35HeT20HYJFJZ5nE'  # Token privado

client = discord.Client()
command_center = CommandCenter(client)
prefix = '!'

def load_commands():
    command_center.add_command(HelpCommand())


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    # ignore message if don't have the prefix !
    if not message.content.startswith(prefix):
        return    
    else: 
       print(message.author)
       print(message.content)
       print('')
    if message.content.startswith(prefix):
        await command_center.process_line(message, message.content)
        
@client.event
async def on_ready():
    print('------')
    print('BadBoy')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('Servers connected to:')
    for server in client.servers:
        print(server)
    print('------')
    await client.change_presence(game=discord.Game(name='Type !help for help page'))
    print('LOGS:\n')

load_commands()
client.run(TOKEN)
