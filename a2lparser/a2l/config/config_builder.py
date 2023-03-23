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


import os


class ConfigBuilder():
    def __init__(self, config, output_filename):
        self.__build_config(cfg=config, file=output_filename)

    def __build_config(self, cfg, file):
        try:
            from a2l.ast.ast_generator import ASTGenerator
            ast_gen = ASTGenerator(cfg, file)
            ast_gen.generate(cleanNames=True)
        except ImportError:
            config.logger.set_level("ERROR")
            config.logger.error("Unable to generate config file")