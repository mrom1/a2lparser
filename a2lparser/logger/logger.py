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
from threading import Lock


class Logger(object):
    Levels = ["none", "ERROR", "WARNING", "INFO", "DEBUG"]
    Format = "[{module}][{level}] {msg}\n"

    def __init__(self, output=sys.stdout):
        self.output = output
        self.level = 0
        self.lock = Lock()

    def new_module(self, module):
        return LoggerModule(self, module)

    def set_level(self, level):
        try:
            index = Logger.Levels.index(level)
        except ValueError:
            return

        self.level = index

    def set_output(self, output):
        self.output = output

    def msg(self, module, level, msg, *args, **kwargs):
        if self.level < level or level > len(Logger.Levels):
            return

        msg = msg.format(*args, **kwargs)

        with self.lock:
            self.output.write(Logger.Format.format(module=module,
                                                   level=Logger.Levels[level],
                                                   msg=msg))
            if hasattr(self.output, "flush"):
                self.output.flush()


class LoggerModule(object):
    def __init__(self, manager, module):
        self.manager = manager
        self.module = module

    def error(self, msg, *args, **kwargs):
        self.manager.msg(self.module, 1, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.manager.msg(self.module, 2, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.manager.msg(self.module, 3, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.manager.msg(self.module, 4, msg, *args, **kwargs)
