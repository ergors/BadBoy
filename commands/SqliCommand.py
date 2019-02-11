import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [url]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://www.diegomacedo.com.br/wp-content/uploads/2016/08/SQLi.jpg")
    embed.add_field(name="Description:".format(alias), value="Test if a url is vulnerable to SQLi.", inline=False)
    embed.add_field(name="Example:", value="!{} http://testphp.vulnweb.com/artists.php?artist=1".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class SqliCommand(CommandBase):

    def __init__(self):
        super(SqliCommand, self).__init__('sqli')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

