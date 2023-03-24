#######################################################################################
# a2lparser: https://github.com/mrom1/a2lparser                                       #
# author: https://github.com/mrom1                                                    #
#                                                                                     #
# This file is part of the a2lparser package.                                         #
#                                                                                     #
# a2lparser is free software: you can redistribute it and/or modify it                #
# under the terms of the GNU General Public License as published by the               #
# Free Software Foundation, either version 3 of the License, or (at your option)      #
# any later version.                                                                  #
#                                                                                     #
# a2lparser is distributed in the hope that it will be useful,                        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY      #
# or FITNESS FOR A PARTICULAR PURPOSE.                                                #
# See the GNU General Public License for more details.                                #
#                                                                                     #
# You should have received a copy of the GNU General Public License                   #
# along with a2lparser. If not, see <https://www.gnu.org/licenses/>.                  #
#######################################################################################


import sys
from typing import TextIO
from threading import Lock
from a2lparser.logger.logger_module import LoggerModule


class Logger:
    """
    Helper class for logging information.

    Usage:
        >>> logger_manager = Logger()
        >>> log = logger.new_module("MODULE")
        >>> log.error("Some error message.")
    """

    Levels = ["none", "ERROR", "WARNING", "INFO", "DEBUG"]
    Format = "[{module}][{level}] {msg}\n"

    def __init__(self, output: TextIO = sys.stdout) -> None:
        """
        Logger Constructor.

        Args:
            - output: TextIO object used for output. Defaults to sys.stdout
        """
        self.output = output
        self.level = 0
        self.lock = Lock()

    def new_module(self, module: str) -> LoggerModule:
        """
        Returns a new LoggerModule with the given module name.
        """
        return LoggerModule(self, module)

    def set_level(self, level: str) -> None:
        """
        Sets the verbositoy level of the logger.

        Args:
            - level: filters the importance of the messages.
                     Values can be "debug", "info", "warning", "error"
        """
        try:
            index = Logger.Levels.index(level)
        except ValueError as ex:
            print(f"Unable to set the Logger level to '{level}': {ex}")
            return

        self.level = index

    def set_output(self, output: TextIO):
        """
        Sets the output medium of the logger.

        Args:
            - output: TextIO buffer which will be written to.
        """
        self.output = output

    def msg(self, module, level, msg, *args, **kwargs):
        """
        Writes a logging message to the output.
        """
        if self.level < level or level > len(Logger.Levels):
            return

        msg = msg.format(*args, **kwargs)

        with self.lock:
            self.output.write(Logger.Format.format(module=module, level=Logger.Levels[level], msg=msg))
            if hasattr(self.output, "flush"):
                self.output.flush()
