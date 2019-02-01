import discord
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [ip]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://d1w82f5xc78wju.cloudfront.net/uploads/targetware/image/file/17520/shodan.master.jpg")
    embed.add_field(name="Description:".format(alias), value="Search host in shodan.", inline=False)
    embed.add_field(name="Example:", value="!{} 127.0.0.1".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class ShodanCommand(CommandBase):

    def __init__(self):
        super(ShodanCommand, self).__init__('shodan')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

