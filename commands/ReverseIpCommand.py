import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [domain|ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="http://www.jacoballred.com/wp-content/uploads/2013/02/reverse-ip-lookup.jpg")
    embed.add_field(name="Description:".format(alias), value="Verify domains in a host.", inline=False)
    embed.add_field(name="Example:", value="!{} google.com".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class ReverseIpCommand(CommandBase):

    def __init__(self):
        super(ReverseIpCommand, self).__init__('reverseip')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

