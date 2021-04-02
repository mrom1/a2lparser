import sys

from a2l.config.config import Config
from logger.logger import Logger

class A2lXml(object):
    def __init__(self, config, encoding='utf-8'):
        self.logger_manager = Logger()
        self.logger = self.logger_manager.new_module("XML")

        self.config = config
        self.encoding = encoding
        self.ElementStack = []


    def output(self, AST, buffer=sys.stdout):
        if not self.config.validateAST(AST):
            self.logger_manager.set_level("ERROR")
            self.logger.error("Abstract Syntax Tree does not contain any valid A2L elements.")
        else:
            buffer.write(('<?xml version="1.0" encoding="' + self.encoding + '"?>').decode(self.encoding))
            buffer.write(('\n' + '<A2L-File>').decode(self.encoding))
            self.parseAST(AST, buf=buffer)
            buffer.write(('\n' + '</A2L-File>').decode(self.encoding))


    def parseAST(self, AST, offset=0, last_offset=0, buf=sys.stdout):
        if hasattr(AST, "children"):
            if AST.__class__.__name__ in self.config.ast_a2l_nodes_opt_only:
                offset = offset - 2
            else:
                self.ElementStack.append(AST.__class__.__name__)

                if AST.__class__.__name__ in self.config.xml_types:
                    n = self.getEncodedValue(AST, "Name")
                    ref = self.config.xml_ref_names[AST.__class__.__name__]
                    if n and ref:
                        buf.write('\n' + (' ' * offset) + '<' + AST.__class__.__name__ + ' ' + ref + '=' + '"' + n + '"' + '>')
                else:
                    buf.write('\n' + (' ' * offset) + '<' + AST.__class__.__name__ + '>')


            if hasattr(AST, "attr_names"):
                if AST.__class__.__name__ in self.config.xml_types_ref:
                    for attr in AST.attr_names:
                        v = getattr(AST, attr)
                        ref = self.config.xml_ref_names[AST.__class__.__name__]
                        if v and ref:
                            if isinstance(v, (list, tuple)):
                                for a in v:
                                    buf.write('\n' + (' ' * (offset + 2)) + '<' + AST.__class__.__name__ + ' ' + ref + '=' + '"' + self.encodeString(self.tryDecodeValue(a)) + '"' + '/>')
                            else:
                                buf.write('\n' + (' ' * (offset + 2)) + '<' + AST.__class__.__name__ + ' ' + ref + '=' + '"' + self.encodeString(self.tryDecodeValue(v)) + '"' + '/>')
                else:
                    for attr in AST.attr_names:
                        v = self.getEncodedValue(AST, attr)
                        if v is not None:
                            buf.write('\n' + (' ' * (offset + 2)) + '<' + attr + '>' + v + '</' + attr + '>')


            for (child_name, child) in AST.children():
                self.parseAST(child,
                              offset=offset + 2,
                              last_offset=offset,
                              buf=buf)
                if len(self.ElementStack) > 0:
                    if child.__class__.__name__ == self.ElementStack[-1]:
                        self.ElementStack.pop()
                        buf.write('\n' + (' ' * (offset + 2)) + '</' + child.__class__.__name__ + '>')


    def getEncodedValue(self, AST, attr):
        var = getattr(AST, attr)
        if var is not None:
            if isinstance(var, (list, tuple)):
                s = ", ".join(map(str, var))
                r = s.replace('"', '')

            else:
                if isinstance(var, str):
                    r = var.replace('"', '')
                else:
                    r = str(var)

            return self.encodeString(self.tryDecodeValue(r))


    def encodeString(self, s):
        try:
            s = s.encode(self.encoding)
        except UnicodeError:
            print("UnicodeError: Failed to encode " + str(s) + " to '" + self.encoding + "'.")

        s = s.replace( '&', '&amp;')
        s = s.replace( '<', '&lt;')
        s = s.replace( '>', '&gt;')
        s = s.replace('"', '&quot;')
        s = s.replace("'", '&apos;')
        return s


    def tryDecodeValue(self, s):
        for codec in ('latin1', 'utf-8', 'iso-8859-1'):
            try:
                s = s.decode(codec, 'strict')
                return s
            except UnicodeError:
                pass
        return s
