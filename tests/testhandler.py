import unittest
import platform
import xml.etree.ElementTree as et
from a2l.xml.a2l_xml import A2lXml

if platform.python_version_tuple()[0] == "2":
    from cStringIO import StringIO
else:
    from io import StringIO


class Testhandler(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(Testhandler, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


    def getXmlFromAst(self, AST):
        if hasattr(self.param, "parser"):
            if hasattr(self.param.parser, "config"):
                buffer = StringIO()
                xml = A2lXml(self.param.parser.config)
                xml.output(AST, buffer=buffer)
                s = buffer.getvalue()
                buffer.close()
                try:
                    tree = et.fromstring(s)
                    return tree
                except:
                    raise RuntimeError()


    # def testFile(self, filebuffer, ast):
    #     print "\nValidating parsed content..."
    #     if self.checkAstForErrors(filebuffer, ast):
    #         print "Testcase successfull!"
    #
    #     if len(self.parser.Ast_Scope_Stack) > 0:
    #         print "AST Stack could not clean up. Printing Stack: "
    #         print self.parser.Ast_Scope_Stack
    #
    #     return ast
    #
    #
    # def checkAstForErrors(self, filebuffer, node):
    #     no_error = True
    #     d = self.getAstObjectsFromFile(filebuffer)
    #     for AstNodeName in d:
    #         self.countAstObjects(node, AstNodeName)
    #
    #         if self.ast_node_counter != d[AstNodeName]:
    #             no_error = False
    #             print "ERROR: Parsed %s %s blocks and read %s from file!" % (self.ast_node_counter, AstNodeName, d[AstNodeName])
    #
    #         self.resetAstObjectsCounter()
    #
    #     return no_error
    #
    #
    # def getAstObjectsFromFile(self, filebuffer):
    #     filebuffer.seek(0)
    #     str = filebuffer.read()
    #     str_no_comments = self.remove_comments(str)
    #
    #     v = []
    #     for AstNodeName in self.ast_node_names_list:
    #
    #         # s = "/begin " + AstNodeName.upper() + "([^" + "/begin " + AstNodeName.upper() + "]*)/end " + AstNodeName.upper()
    #         s = "/begin " + AstNodeName.upper()
    #         v.append(sum(1 for _ in re.finditer(r'%s\b' % re.escape(s), str_no_comments, re.MULTILINE)))
    #
    #     return dict(zip(self.ast_node_names_list, v))
    #
    #
    # def countAstObjects(self, AstObject, AstNodeName):
    #     if hasattr(AstObject, "children"):
    #         children = AstObject.children()
    #         for (child_name, child) in children:
    #             if child.__class__.__name__ == AstNodeName:
    #                 self.ast_node_counter += 1
    #
    #             self.countAstObjects(child, AstNodeName)
    #
    #
    # def resetAstObjectsCounter(self):
    #     self.ast_node_counter = 0
    #
    #
    # def remove_comments(self, text):
    #     pattern = r"""
    #                             ##  --------- COMMENT ---------
    #            /\*              ##  Start of /* ... */ comment
    #            [^*]*\*+         ##  Non-* followed by 1-or-more *'s
    #            (                ##
    #              [^/*][^*]*\*+  ##
    #            )*               ##  0-or-more things which don't start with /
    #                             ##    but do end with '*'
    #            /                ##  End of /* ... */ comment
    #          |                  ##  -OR-  various things which aren't comments:
    #            (                ##
    #                             ##  ------ " ... " STRING ------
    #              "              ##  Start of " ... " string
    #              (              ##
    #                \\.          ##  Escaped char
    #              |              ##  -OR-
    #                [^"\\]       ##  Non "\ characters
    #              )*             ##
    #              "              ##  End of " ... " string
    #            |                ##  -OR-
    #                             ##
    #                             ##  ------ ' ... ' STRING ------
    #              '              ##  Start of ' ... ' string
    #              (              ##
    #                \\.          ##  Escaped char
    #              |              ##  -OR-
    #                [^'\\]       ##  Non '\ characters
    #              )*             ##
    #              '              ##  End of ' ... ' string
    #            |                ##  -OR-
    #                             ##
    #                             ##  ------ ANYTHING ELSE -------
    #              .              ##  Anything other char
    #              [^/"'\\]*      ##  Chars which doesn't start a comment, string
    #            )                ##    or escape
    #     """
    #     regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    #     noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]
