import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="http://ninjadolinux.com.br/wp-content/uploads/2017/03/top.ten_.tools_.nmap_-768x432.png")
    embed.add_field(name="Description:".format(alias), value="Simple port scan an ip address.", inline=False)
    embed.add_field(name="Example:", value="!{} 127.0.0.1".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class NmapCommand(CommandBase):

    def __init__(self):
        super(NmapCommand, self).__init__('nmap')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

