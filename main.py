#!/usr/bin/python3
# -*- encoding: utf-8 -*_
# BadBoy Bot
# Funcionando em Python 3.6
import discord
from commands.framework.CommandCenter import CommandCenter

TOKEN = 'NTE5MTk3ODI2NTY0MDk2MDMw.Dwhy1w.SI3U2z9Y5tX35HeT20HYJFJZ5nE'  # Token privado

client = discord.Client()
command_center = CommandCenter(client)
prefix = '!'

def load_commands():
    command_center.add_command(None)


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
    if message.content.startswith(prefix + "hello"):
        msg = "Hello {0.author.mention} ``test`` **a** :poop:".format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith(prefix):
        command_center.process_line(message, message.content)

    if message.content.startswith(prefix + "help"):
        embed = discord.Embed(
            title="Help Page",
            description="Prefix: **!**",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/519223258428735511/520234344313257984/badboy.jpg")
        embed.add_field(name="!whois", value="Verify informations abou the site.", inline=False)
        embed.add_field(name="!geoip", value="GeoIp lookup.", inline=False)
        embed.add_field(name="!nmap", value="Simple port scan an ip address.", inline=False)
        embed.add_field(name="!sqli", value="Test if a url is SQLi vulnerable.", inline=False)
        embed.add_field(name="!shodan", value="Search query in shodan.", inline=False)
        embed.add_field(name="!exploitdb", value="Search exploits in ExploitDB", inline=False)
        embed.add_field(name="!sites", value="Verify sites in a host.", inline=False)
        embed.set_footer(text="Type !help [command] for more info about command")
        await client.send_message(message.channel, embed=embed)


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
