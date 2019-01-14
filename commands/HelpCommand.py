import discord

from commands.framework.CommandBase import CommandBase


class HelpCommand(CommandBase):

    def __init__(self):
        super(HelpCommand, self).__init__('teste')

    async def execute(self, client, message, args):
        print('executing teste command')
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
