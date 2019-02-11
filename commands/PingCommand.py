import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://buffered.com/wp-content/uploads/2018/02/shutterstock_224474662-e1519152637664.jpg")
    embed.add_field(name="Description:".format(alias), value="Ping some target.", inline=False)
    embed.add_field(name="Example:", value="!{} 127.0.0.1".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class PingCommand(CommandBase):

    def __init__(self):
        super(PingCommand, self).__init__('ping')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

