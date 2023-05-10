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


from a2lparser.a2l.lex.keywords.a2l_keywords_types import A2LKeywordsTypes
from a2lparser.a2l.lex.keywords.a2l_keywords_enums import A2LKeywordsEnums
from a2lparser.a2l.lex.keywords.a2l_keywords_sections import A2LKeywordsSections
from a2lparser.a2l.lex.keywords.a2l_keywords_datatypes import A2LKeywordsDataTypes


class LexerKeywords:
    """
    Holds a collection of keyword tokens used in an A2L file.
    """

    keywords_type: list = A2LKeywordsTypes.keywords
    keywords_enum: list = A2LKeywordsEnums.keywords
    keywords_section: list = A2LKeywordsSections.keywords
    keywords_datatypes: list = A2LKeywordsDataTypes.keywords
