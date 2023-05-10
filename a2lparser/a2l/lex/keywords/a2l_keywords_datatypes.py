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


class A2LKeywordsDataTypes:
    """
    Keywords for parsing A2L data types like "BYTE", "LONG" etc.
    """

    keywords: list = [
        # atatypes
        "SBYTE",
        "UBYTE",
        "UWORD",
        "SWORD",
        "ULONG",
        "SLONG",
        "A_UINT64",
        "A_INT64",
        "FLOAT32_IEEE",
        "FLOAT64_IEEE",
        # datasizes
        "BYTE",
        "WORD",
        "LONG",
        # addrtypes
        "PBYTE",
        "PWORD",
        "PLONG",
        "DIRECT",
        # byteoders
        "LITTLE_ENDIAN",
        "BIG_ENDIAN",
        "MSB_LAST",
        "MSB_FIRST",
        # indexorders
        "INDEX_INCR",
        "INDEX_DECR",
        # attributes
        "INTERN",
        "EXTERN",
    ]
