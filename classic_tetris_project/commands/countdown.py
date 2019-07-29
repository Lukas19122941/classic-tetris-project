import time

from .command import Command, CommandException, register_command
from ..util import Platform

@register_command(*map(str, range(3, 11)))
class Countdown(Command):
    
    @property
    def supported_platforms(self):
        return [Platform.TWITCH]
    
    def execute(self):
        self.check_moderator()
        n = int(self.context.command_name)
        for i in range(n, 0, -1):
            self.send_message(str(i))
            time.sleep(1)
        self.send_message("Tetris!")
