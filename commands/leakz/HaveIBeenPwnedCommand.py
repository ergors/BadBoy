import discord
import requests
import re
from commands.framework.CommandBase import CommandBase


async def show_command_help(client, message, alias):
    embed = discord.Embed(
        title="Command \"{}\" Help".format(alias.capitalize()),
        description="Usage: !{} [email]".format(alias),
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(
        url="https://haveibeenpwned.com/Content/Images/SocialLogo.png")
    embed.add_field(name="Description:".format(alias), value="Checks if a given email has leaked credentials.",
                    inline=False)
    embed.add_field(name="Example:", value="!{} me@domain.net".format(alias), inline=True)
    embed.set_footer(text="Type !help to see all commands.")
    await client.send_message(message.channel, embed=embed)


class HaveIBeenPwnedCommand(CommandBase):

    def __init__(self):
        super(HaveIBeenPwnedCommand, self).__init__('leaked', 'hibp')

    async def execute(self, client, message, args):
        if not args:
            await show_command_help(client, message, self.alias_used)
            return

        email = args[0]
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            await client.send_message(message.channel, ':x: | _E-mail address not valid.._')
            return

        response = requests.get('https://lea.kz/api/mail/{}'.format(email))
        if response.status_code == 404:
            await client.send_message(message.channel, ':x: | _No leakage records._')
            return

        await client.send_message(message.channel, ':globe_with_meridians: | _Records found on websites: {}_'.format(
            response.json()['leaked']))
