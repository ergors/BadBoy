import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [domain | ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://www.freewebmentor.com/wp-content/uploads/2014/10/whois-logo.jpg")
    embed.add_field(name="Description:".format(alias), value="Checks information about a given domain.", inline=False)
    embed.add_field(name="Example:", value="!{} 8.8.8.8".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class WhoisCommand(CommandBase):

    def __init__(self):
        super(WhoisCommand, self).__init__('whois')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return
