

class CommandCenter(object):

    commands = dict()
    discord_client = None

    def __init__(self, discord_client):
        self.discord_client = discord_client

    async def process_line(self, message, line):
        print('processing line {}'.format(line))
        command_name = line[1:]
        args = None

        if ' ' in command_name:
            command_name = command_name.split(' ')[0]
            args = line[line.index(' ') + 1:].split(' ')

        if command_name.lower() in self.commands:
            command = self.commands[command_name.lower()]
            await command.execute(self.discord_client, message, args)

    def add_command(self, command):
        for alias in command.get_aliases():
            self.commands[alias.lower()] = command
            command.set_command_center(self)
