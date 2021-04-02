import glob, os, time

from logger.logger import Logger
from a2l.config.config import Config
from a2l.a2l_yacc import A2lYacc
from a2l.xml.a2l_xml import A2lXml


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
        # self.parser = A2lParser(config=config,
        #                         lex_optimize=config.optimize,
        #                         yacc_optimize=config.optimize,
        #                         taboutputdir=config.gen_dir,
        #                         gen_tables=config.write_tables,
        #                         debug_output=config.debug_active,
        #                         error_resolve=config.error_resolve_active
        #                         )

    def parseFile(self, fileName, xmlFileName=''):
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
                        #t_start = time.time()
                        abstract_syntax_tree = self.__timeFunction( self.parser.parse,
                                                                    filename=file,
                                                                    start_of_a2ml=start_of_a2ml_section,
                                                                    end_of_a2ml=end_of_a2ml_section,
                                                                    input_string=input_string,
                                                                    filelength=file_length
                                                                    )
                        # abstract_syntax_tree = self.parser.parse(filename=file,
                        #                                          start_of_a2ml=start_of_a2ml_section,
                        #                                          end_of_a2ml=end_of_a2ml_section,
                        #                                          input_string=input_string,
                        #                                          filelength=file_length)
                        #t_end = time.time()
                        #print "\n"
                        #self.logger.info("elapsed time: %s %s" %((t_end -t_start), "sec"))

                        self.logger.info("Creating XML File...")
                        # t_start = time.time()
                        xmlFileName = self.__timeFunction(  self.__printXml,
                                                            fileName=file,
                                                            xmlFileName=xmlFileName,
                                                            AstObject=abstract_syntax_tree
                                                          )
                        # xmlFileName = self.__printXml(fileName=file,
                        #                               xmlFileName=xmlFileName,
                        #                               AstObject=abstract_syntax_tree)

                        self.logger.info("XML File: " + xmlFileName + " created.")
                        # t_end = time.time()
                        # self.logger.info("elapsed time: %s %s" % ((t_end - t_start), "sec"))

                        # if self.testcase:
                        #     try:
                        #         os.remove(xmlFileName)
                        #     except OSError:
                        #         pass

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
