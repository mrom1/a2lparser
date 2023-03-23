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


import glob, os, time
from a2lparser.logger.logger import Logger
from a2lparser.a2l.config.config import Config
from a2lparser.a2l.a2l_yacc import A2lYacc
from a2lparser.a2l.xml.a2l_xml import A2lXml


class Parser(object):
    """
    """
    def __init__(self, config):
        self.logger_manager = Logger()
        self.logger_manager.set_level("INFO")
        self.logger = self.logger_manager.new_module("PARSER")

        if config.verbosity > 1:
            self.logger.info("Initializing Parser ...")

        self.parser = A2lYacc(config=config)


    def parseFile(self, fileName, xmlFileName='', createXML=True):
        for file in glob.glob(fileName):
            if os.path.exists(file):
                try:
                    with open(file) as f:
                        [start_of_a2ml_section, end_of_a2ml_section] = self.__getA2mlSectionIndex(f)
                        input_string = self.__extractA2mlSection(f)
                        file_length = self.__getFileLength(f)
                        f.seek(0)
                        file_length_2 =f.read().count('\n')

                        self.logger.info("Parsing file: " + file)
                        abstract_syntax_tree = self.__timeFunction( self.parser.parse,
                                                                    filename=file,
                                                                    start_of_a2ml=start_of_a2ml_section,
                                                                    end_of_a2ml=end_of_a2ml_section,
                                                                    input_string=input_string,
                                                                    filelength=file_length
                                                                    )
                        if createXML:
                            self.logger.info("Creating XML File...")
                            xmlFileName = self.__timeFunction(  self.__printXml,
                                                                fileName=file,
                                                                xmlFileName=xmlFileName,
                                                                AstObject=abstract_syntax_tree
                                                              )
                            self.logger.info("XML File: " + xmlFileName + " created.")
                        
                        return abstract_syntax_tree

                except IOError as e:
                    print(e.errno)
                    print(e)
            else:
                self.logger.info("File " + fileName + " does not exist.")


    def __timeFunction(self, func, *args, **kwargs):
        if self.parser.config.verbosity > 1:
            self.logger_manager.set_level("INFO")
            t_start = time.time()
            r = func(*args, **kwargs)
            t_end = time.time()
            self.logger.info("elapsed time: %s %s" %((t_end -t_start), "sec"))
            return r
        else:
            return func(*args, **kwargs)


    def __printXml(self, fileName, xmlFileName, AstObject):
        try:
            if len(xmlFileName) == 0:
                xmlFileName = os.path.splitext(fileName)[0] + '.xml'
            with open(xmlFileName, 'w') as f:
                xml = A2lXml(self.parser.config)
                xml.output(AST=AstObject,
                               buffer=f)
            return xmlFileName

        except IOError as e:
            print(e.errno)
            print(e)


    def __extractA2mlSection(self, filebuffer):
        filebuffer.seek(0)
        str = filebuffer.read()
        if "/begin A2ML" in str and "/end A2ML" in str:
            pre_a2ml = str[0:str.index("/begin A2ML")]
            str = pre_a2ml + str[(str.index("/end A2ML") + len("/end A2ML")):]
        return str


    def __getA2mlSectionIndex(self, filebuffer):
        filebuffer.seek(0)
        text = filebuffer.read()
        start_of_a2ml = 0
        end_of_a2ml = 0

        if "/begin A2ML" in text:
            for num, line in enumerate(filebuffer, 1):
                if line.strip() == "/begin A2ML":
                    start_of_a2ml = num
                elif line.strip() == "/end A2ML":
                    end_of_a2ml = num
                    break

        return [start_of_a2ml, end_of_a2ml]


    def __getFileLength(self, filebuffer):
        filebuffer.seek(0)
        return sum(1 for line in filebuffer)
