import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message):
    embed = discord.Embed(
        title='Whois Command',
        description='Whois Command Help',
        color=discord.Colour.red()
    )
    # TODO Customizar a mensagem de ajuda do comando.


class WhoisCommand(CommandBase):

    def __init__(self):
        super(WhoisCommand, self).__init__('whois')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message)
            return
