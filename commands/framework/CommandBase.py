from commands.framework.Command import Command


class CommandBase(Command):
    aliases = list()
    alias_used = str()
    command_center = None

    def __init__(self, *aliases):
        super(CommandBase, self).__init__()
        self.aliases = aliases

    def get_aliases(self):
        return self.aliases

    def set_command_center(self, command_center):
        self.command_center = command_center

    def set_alias_used(self, alias_used):
        self.alias_used = alias_used
