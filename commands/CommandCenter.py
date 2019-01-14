

class CommandCenter(object):

    commands = dict()
    discord_client = None

    def __init__(self, discord_client):
        self.discord_client = discord_client

    def process_line(self, message, line):
        command_name = line[1:]
        args = None

        if ' ' in command_name:
            command_name = command_name.split(' ')[0]
            args = line[line.index(' ') + 1:].split(' ')

        command = self.commands[command_name.lower()]
        if command is not None:
            command.execute(message, args)
