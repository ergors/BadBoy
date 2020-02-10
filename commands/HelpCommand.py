import discord

from commands.framework.CommandBase import CommandBase


class HelpCommand(CommandBase):

    def __init__(self):
        super(HelpCommand, self).__init__('help')

    async def execute(self, client, message, args):
        embed = discord.Embed(
            title="Help Page",
            description="Prefix: **!**",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/519223258428735511/520234344313257984/badboy.jpg")
        embed.add_field(name="!whois", value="Verify informations abou the site.", inline=True)
        embed.add_field(name="!ping", value="Ping some target.", inline=True)
        embed.add_field(name="!hibp", value="Check if your email got leaked.", inline=True)
        embed.add_field(name="!geoip", value="GeoIp lookup.", inline=True)
        embed.add_field(name="!nmap", value="Simple port scan an ip address.", inline=True)
        embed.add_field(name="!sqli", value="Test if a url is vulnerable to SQLi.", inline=True)
        embed.add_field(name="!shodan", value="Search host in shodan.", inline=True)
        embed.add_field(name="!exploitdb", value="Search exploits in ExploitDB.", inline=True)
        embed.add_field(name="!reverseip", value="Verify domains in a host.", inline=True)
        embed.set_footer(text="Type ![command] for more info about command")
        await client.send_message(message.channel, embed=embed)
