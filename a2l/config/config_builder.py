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