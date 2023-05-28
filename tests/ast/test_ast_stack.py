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


from a2lparser.a2l.ast.ast_stack import ASTStack


def test_ast_stack_complete_section():
    """
    @TODO
    """
    input_tokens = """
    /begin DATA
        DATA_LABEL "data"
        DATA_ORIGIN "pdf"
        /begin DATA_TEXT
            "data text example1"
            "data text example2"
        /end DATA_TEXT
        DATA_VALUE 0x004488eeff
    /end DATA
    """
    stack = ASTStack()

    for token in input_tokens:
        if token.startswith("/begin"):
            # Simulate a begin section trigger.
            next_token = next(input_tokens)
            stack.feed_token(token)
            stack.feed_token(next_token)
            # feeding the two tokens "/begin", followed by KEYWORD should trigger ASTStack
            # to build a dictionary with the key "DATA" or "DATA_TEXT"
            # internally a function ASTStack.push_section is called.
            if next_token == "DATA":
                # stack should contain an empty dictionary with a "DATA" key
                assert stack["DATA"]
            elif next_token == "DATA_TEXT":
                # stack should contain a dictionary with a "DATA" key
                # and a "DATA_TEXT" dictionary under it
                assert stack["DATA"]
                assert stack["DATA"]["DATA_TEXT"]

        elif token.startswith("/end"):
            # Simulate a end section trigger.
            stack.feed_token(token)
            stack.feed_token(next(input_tokens))
            # feeding the two tokens "/end", followed by KEYWORD should trigger ASTStack
            # to delete a dictionary with the key KEYWORD
            # internally a function ASTStack.pop_section is called.
            if next_token == "DATA_TEXT":
                # At this point the "DATA_TEXT" dictionary under the "DATA" dictionary should not exist anymore.
                assert "DATA_TEXT" not in stack
            elif next_token == "DATA":
                # The "DATA" section is over and should have been removed from the dictionary now.
                assert "DATA" not in stack
                assert len(stack) == 0

    # input_tokens = """
    # /begin ANNOTATION
    #     ANNOTATION_LABEL "annotation test label"
    #     /begin ANNOTATION_TEXT
    #         "annotation text example"
    #     /end ANNOTATION_TEXT
    #     ANNOTATION_ORIGIN "annotation test origin"
    # /end ANNOTATION
    # """
