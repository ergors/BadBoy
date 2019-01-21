import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1uWBaRIo9vCupzdh0TTwEnf-SIhfsDFrzHL5gp7U8lU5y_9r2")
    embed.add_field(name="Description:".format(alias), value="GeoIp lookup.", inline=False)
    embed.add_field(name="Example:", value="!{} 172.217.28.14".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class GeoCommand(CommandBase):

    def __init__(self):
        super(GeoCommand, self).__init__('geoip')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

