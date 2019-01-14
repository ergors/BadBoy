from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_command_center(self, command_center):
        """ setter para o command center """

    @abstractmethod
    def execute(self, client, message, args):
        """ executor de comandos """

    @abstractmethod
    def get_aliases(self):
        """ getter para os aliases do comando """

    @abstractmethod
    def set_alias_used(self, alias):
        """ setter para o alias usado """
