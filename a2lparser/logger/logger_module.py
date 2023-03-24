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


class LoggerModule:
    """
    Provides utility for the Logger class.
    Represents the LoggerModule which holds the instance for the message methods.
    """

    def __init__(self, manager, module) -> None:
        """
        LoggerModule Constructor.

        Args:
            - manager: A reference to the Logger class which manages the stream.
            - module: The name of the module which this will be registered to.
        """
        self.manager = manager
        self.module = module

    def error(self, msg, *args, **kwargs) -> None:
        """
        Prints the message to the error channel.
        """
        self.manager.msg(self.module, 1, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs) -> None:
        """
        Prints the message to the warning channel.
        """
        self.manager.msg(self.module, 2, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs) -> None:
        """
        Prints the message to the info channel.
        """
        self.manager.msg(self.module, 3, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs) -> None:
        """
        Prints the message to the debug channel.
        """
        self.manager.msg(self.module, 4, msg, *args, **kwargs)
