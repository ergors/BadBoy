#!/usr/bin/python3
# -*- encoding: utf-8 -*_
# BadBoy Bot
# Funcionando em Python 3.6
import discord
import os

#Load Commands
from commands.HelpCommand import HelpCommand
from commands.ShodanCommand import ShodanCommand
from commands.WhoisCommand import WhoisCommand
from commands.NmapCommand import NmapCommand
from commands.framework.CommandCenter import CommandCenter
from commands.GeoCommand import GeoCommand
from dotenv import load_dotenv
from commands.leakz.HaveIBeenPwnedCommand import HaveIBeenPwnedCommand

load_dotenv()  # Carrega as configurações do arquivo .env. Caso você não o possua, copie-o do arquivo .env.example

TOKEN = os.getenv('PRIVATE_TOKEN')

client = discord.Client()
command_center = CommandCenter(client)
prefix = '!'


def load_commands():
    command_center.add_command(ShodanCommand())
    command_center.add_command(HelpCommand())
    command_center.add_command(WhoisCommand())
    command_center.add_command(NmapCommand())
    command_center.add_command(HaveIBeenPwnedCommand())
    command_center.add_command(GeoCommand())


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
    print('\033[91m')
    print('  /$$$$$$$                  /$$ /$$$$$$$                      ')
    print(' | $$__  $$                | $$| $$__  $$                     ')
    print(' | $$  \ $$  /$$$$$$   /$$$$$$$| $$  \ $$  /$$$$$$  /$$   /$$ ')
    print(' | $$$$$$$  |____  $$ /$$__  $$| $$$$$$$  /$$__  $$| $$  | $$ ')
    print(' | $$__  $$  /$$$$$$$| $$  | $$| $$__  $$| $$  \ $$| $$  | $$ ')
    print(' | $$  \ $$ /$$__  $$| $$  | $$| $$  \ $$| $$  | $$| $$  | $$ ')
    print(' | $$$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$/|  $$$$$$$ ')
    print(' |_______/  \_______/ \_______/|_______/  \______/  \____  $$ ')
    print('                                                    /$$  | $$ ')
    print('                                                   |  $$$$$$/ ')
    print('                                                    \______/  ')
    x = discord.__version__
    print('\033[0mVersion: \033[91m{}'.format(x))
    print('\033[0mServers connected to:')
    for server in client.servers:
        print(server)
    await client.change_presence(game=discord.Game(name='Type !help for help page'))
    print('\nLOGS:\n')


load_commands()
client.run(TOKEN)
